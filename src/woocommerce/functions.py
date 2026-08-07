from src.woocommerce.client import WooCommerceClient
from datetime import datetime, timedelta
from typing import List, Dict, Any
import pandas as pd

client = WooCommerceClient()

def get_top_products(period: str = 'week', limit: int = 10) -> List[Dict[str, Any]]:
    """
    Получить топ товары за период.
    period: 'week', 'month', 'year'
    limit: количество товаров
    """
    try:
        products = client.get_products(limit=limit, orderby='popularity')
        
        result = []
        for product in products:
            result.append({
                'id': product['id'],
                'name': product['name'],
                'price': product['price'],
                'rating': product.get('average_rating', 0),
                'sales': product.get('total_sales', 0),
            })
        
        return result
    except Exception as e:
        return [{'error': str(e)}]

def find_suspicious_orders() -> List[Dict[str, Any]]:
    """
    Найти подозрительные заказы (большая сумма, новый клиент, и т.д.)
    """
    try:
        orders = client.get_orders(limit=100, status='any')
        
        suspicious = []
        for order in orders:
            total = float(order.get('total', 0))
            
            # Критерии подозрительности
            if total > 5000:  # Большая сумма
                suspicious.append({
                    'order_id': order['id'],
                    'customer': order.get('billing', {}).get('email', 'N/A'),
                    'total': total,
                    'status': order['status'],
                    'reason': 'High order amount'
                })
        
        return suspicious
    except Exception as e:
        return [{'error': str(e)}]

def get_product_stats(period: str = 'week') -> Dict[str, Any]:
    """
    Получить статистику по товарам
    """
    try:
        products = client.get_products(limit=100)
        
        total_revenue = sum(float(p.get('price', 0)) * p.get('total_sales', 0) for p in products)
        avg_price = sum(float(p.get('price', 0)) for p in products) / len(products) if products else 0
        
        return {
            'total_products': len(products),
            'total_revenue': round(total_revenue, 2),
            'average_price': round(avg_price, 2),
            'period': period
        }
    except Exception as e:
        return {'error': str(e)}
def generate_product_description(product_name: str, features: str = "") -> Dict[str, Any]:
    """
    Сгенерировать SEO-описание для нового товара.
    product_name: название товара (например 'Красная футболка')
    features: ключевые характеристики через запятую (например 'хлопок, размер M, приталенная')
    """
    return {
        "product_name": product_name,
        "features": features,
        "task": "generate_description"
    }