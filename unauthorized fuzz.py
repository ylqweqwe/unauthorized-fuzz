import requests
from decouple import config


BASE_URL = config('BASE_URL', default='')
HEADERS = {
    'auto': config('API_TOKEN', default='your_token_here'), 
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
COOKIES = {
    'session_id': config('SESSION_COOKIE', default='your_cookie_here')
}


API_ENDPOINTS = [
  
]

def send_request(method, url, headers=None, cookies=None, **kwargs):

    try:
        response = requests.request(
            method,
            url,
            headers=headers or HEADERS,
            cookies=cookies or COOKIES,
            timeout=10,
            verify=True, 
            **kwargs
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return f"HTTP错误: {e.response.status_code} - {e.response.text}"
    except requests.exceptions.RequestException as e:
        return f"请求失败: {str(e)}"

def main():

    custom_headers = {
        **HEADERS,
        'X-Custom-Header': 'custom_value'
    }
    
    custom_cookies = {
        **COOKIES,
        'new_cookie': 'cookie_value'
    }
    
    for endpoint in API_ENDPOINTS:
        full_url = BASE_URL + endpoint
        
        print(f"\n===> 处理接口: {endpoint}")
        
        get_response = send_request(
            "GET",
            full_url,
            headers=custom_headers,
            cookies=custom_cookies
        )
        print(f"GET响应状态码: {get_response.get('code', 'N/A')}")
        

        post_data = {
            "key1": "value1",
            "key2": ["list_item1", "list_item2"]
        }
        post_response = send_request(
            "POST",
            full_url,
            headers={**custom_headers, 'Content-Type': 'application/json'},
            cookies=custom_cookies,
            json=post_data
        )
        print(f"POST响应状态码: {post_response.get('code', 'N/A')}")

if __name__ == "__main__":
    main()
