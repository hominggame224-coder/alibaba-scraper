"""
Alibaba Game Machine & Amusement Machine Data Scraper
自动爬取阿里巴巴游戏机和娱乐设备的商品数据
"""

import requests
import pandas as pd
from bs4 import BeautifulSoup
import time
from datetime import datetime
import json
import os
from pathlib import Path
import logging

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class AlibabaGameMachineScraper:
    def __init__(self):
        self.base_url = "https://www.alibaba.com/trade/search"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        self.data = []
        self.keywords = ['game machine', 'amusement game machine']
        
    def scrape_products(self, keyword, pages=10):
        """
        爬取指定关键词的商品数据
        
        Args:
            keyword: 搜索关键词
            pages: 爬取页数（每页通常20个商品）
        """
        logger.info(f"开始爬取关键词: {keyword}")
        
        for page in range(1, pages + 1):
            try:
                # 构建搜索URL
                params = {
                    'SearchText': keyword,
                    'pageNumber': page,
                    'pageSize': '50'  # 每页50条
                }
                
                url = f"{self.base_url}?SearchText={keyword}&pageNumber={page}"
                
                logger.info(f"正在爬取第 {page} 页...")
                
                # 发送请求
                response = requests.get(url, headers=self.headers, timeout=10)
                response.encoding = 'utf-8'
                
                if response.status_code != 200:
                    logger.warning(f"页面 {page} 返回状态码: {response.status_code}")
                    continue
                
                # 解析HTML
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # 查找商品列表 (阿里巴巴可能需要调整选择器)
                products = soup.find_all('div', {'data-component-type': 'organic'})
                
                if not products:
                    logger.warning(f"页面 {page} 未找到商品数据，可能需要调整选择器")
                    # 尝试备用选择器
                    products = soup.find_all('div', class_='search-item-card')
                
                if not products:
                    logger.info(f"页面 {page} 无更多商品数据，停止爬取")
                    break
                
                # 提取商品信息
                for product in products:
                    try:
                        product_data = self.extract_product_info(product, keyword)
                        if product_data:
                            self.data.append(product_data)
                            logger.info(f"已提取: {product_data['product_title'][:50]}...")
                    except Exception as e:
                        logger.warning(f"提取商品信息失败: {e}")
                        continue
                
                # 随机延迟，避免被封IP
                time.sleep(2 + (page % 3))  # 2-5秒随机延迟
                
            except Exception as e:
                logger.error(f"爬取第 {page} 页时出错: {e}")
                continue
    
    def extract_product_info(self, product_element, keyword):
        """
        从单个产品元素提取信息
        """
        try:
            product_data = {}
            
            # 商品标题
            title_elem = product_element.find('h2', class_='search-card-e-title')
            if not title_elem:
                title_elem = product_element.find('h2')
            product_data['product_title'] = title_elem.get_text(strip=True) if title_elem else 'N/A'
            
            # 商品链接
            link_elem = product_element.find('a', {'data-component-type': 'organic'})
            if not link_elem:
                link_elem = product_element.find('a', class_='search-card-e-title-a')
            product_data['product_url'] = link_elem.get('href', 'N/A') if link_elem else 'N/A'
            
            # 价格
            price_elem = product_element.find('span', class_='search-card-e-price-main')
            if not price_elem:
                price_elem = product_element.find('span', class_='search-card-e-price')
            product_data['price'] = price_elem.get_text(strip=True) if price_elem else 'N/A'
            
            # 店铺名称
            shop_elem = product_element.find('a', class_='search-card-e-company')
            if not shop_elem:
                shop_elem = product_element.find('span', class_='search-card-e-company')
            product_data['shop_name'] = shop_elem.get_text(strip=True) if shop_elem else 'N/A'
            
            # 成交量 (可能显示为"xxx已售" 或 "xxx交易")
            transaction_elem = product_element.find('span', class_='search-card-e-stamps')
            if transaction_elem:
                transaction_text = transaction_elem.get_text(strip=True)
                product_data['transactions'] = transaction_text
            else:
                product_data['transactions'] = 'N/A'
            
            # 评分
            rating_elem = product_element.find('span', class_='search-card-e-rating')
            if not rating_elem:
                rating_elem = product_element.find('span', class_='search-card-e-rate-score')
            product_data['rating'] = rating_elem.get_text(strip=True) if rating_elem else 'N/A'
            
            # 评价数
            review_count_elem = product_element.find('span', class_='search-card-e-rate-count')
            if review_count_elem:
                review_text = review_count_elem.get_text(strip=True)
                product_data['review_count'] = review_text
            else:
                product_data['review_count'] = 'N/A'
            
            # 添加元数据
            product_data['keyword'] = keyword
            product_data['scraped_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            return product_data
            
        except Exception as e:
            logger.error(f"提取产品信息失败: {e}")
            return None
    
    def save_to_csv(self, filename='alibaba_game_machines.csv'):
        """
        将爬取的数据保存为CSV文件
        """
        if not self.data:
            logger.warning("没有数据可保存")
            return
        
        try:
            df = pd.DataFrame(self.data)
            
            # 创建data目录如果不存在
            Path('data').mkdir(exist_ok=True)
            
            # 保存为CSV
            filepath = f'data/{filename}'
            df.to_csv(filepath, index=False, encoding='utf-8-sig')
            logger.info(f"数据已保存到: {filepath}")
            logger.info(f"总共提取: {len(self.data)} 条商品数据")
            
            return filepath
            
        except Exception as e:
            logger.error(f"保存CSV失败: {e}")
            return None
    
    def save_to_json(self, filename='alibaba_game_machines.json'):
        """
        将爬取的数据保存为JSON文件
        """
        if not self.data:
            logger.warning("没有数据可保存")
            return
        
        try:
            Path('data').mkdir(exist_ok=True)
            filepath = f'data/{filename}'
            
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(self.data, f, ensure_ascii=False, indent=2)
            
            logger.info(f"JSON数据已保存到: {filepath}")
            return filepath
            
        except Exception as e:
            logger.error(f"保存JSON失败: {e}")
            return None
    
    def run(self, max_products=500):
        """
        运行爬虫，爬取指定数量的商品
        
        Args:
            max_products: 最大爬取商品数 (默认500个)
        """
        logger.info(f"开始爬取 {max_products} 个商品")
        logger.info(f"关键词: {self.keywords}")
        
        # 计算需要爬取的页数 (每页50条)
        pages_needed = (max_products // 50) + 1
        
        for keyword in self.keywords:
            if len(self.data) >= max_products:
                break
            
            # 计算该关键词还需爬取多少条
            remaining = max_products - len(self.data)
            pages_for_keyword = (remaining // 50) + 1
            
            self.scrape_products(keyword, pages=pages_for_keyword)
        
        # 截断到指定数量
        self.data = self.data[:max_products]
        
        # 保存数据
        csv_file = self.save_to_csv(f'alibaba_game_machines_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv')
        json_file = self.save_to_json(f'alibaba_game_machines_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json')
        
        logger.info(f"爬虫任务完成！共提取 {len(self.data)} 条数据")
        return csv_file, json_file


def main():
    """主入口函数"""
    try:
        scraper = AlibabaGameMachineScraper()
        scraper.run(max_products=500)
        logger.info("爬虫执行成功")
    except Exception as e:
        logger.error(f"爬虫执行失败: {e}")
        raise


if __name__ == '__main__':
    main()
