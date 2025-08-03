#!/usr/bin/env python3
"""
Test script to verify the Free Fire Like Bot API functionality
"""

import asyncio
import aiohttp
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

async def test_api():
    """Test the Free Fire Like API endpoint"""
    
    api_host = os.getenv('API_HOST', 'https://likexthug.vercel.app')
    api_key = os.getenv('RAPIDAPI_KEY', 'GREAT')
    
    print("🔍 Testing Free Fire Like API...")
    print(f"API Host: {api_host}")
    print(f"API Key: {api_key}")
    print("-" * 50)
    
    try:
        async with aiohttp.ClientSession() as session:
            url = f"{api_host}/like"
            params = {
                'uid': '2537964178',  # Test UID
                'region': 'ind',  # Default region (India)
                'key': api_key
            }
            
            print(f"Making request to: {url}")
            print(f"Parameters: {params}")
            print("-" * 50)
            
            async with session.get(url, params=params) as response:
                print(f"Response Status: {response.status}")
                
                if response.status == 200:
                    data = await response.json()
                    print("✅ API Response Success!")
                    print(json.dumps(data, indent=2))
                    
                    # Extract key information
                    player = data.get('player', {})
                    likes = data.get('likes', {})
                    api_info = data.get('api_key_details', {})
                    
                    print("\n📊 Summary:")
                    print(f"Player UID: {player.get('uid', 'N/A')}")
                    print(f"Player Region: {player.get('region', 'N/A')}")
                    print(f"Player Nickname: {player.get('nickname', 'N/A')}")
                    print(f"Likes Before: {likes.get('before', 0):,}")
                    print(f"Likes After: {likes.get('after', 0):,}")
                    print(f"Likes Added: {likes.get('added_by_api', 0)}")
                    print(f"API Usage: {api_info.get('current_usage', 0)}/{api_info.get('usage_limit', 0)}")
                    
                else:
                    print(f"❌ API Error: Status {response.status}")
                    error_text = await response.text()
                    print(f"Error Response: {error_text}")
                    
    except aiohttp.ClientError as e:
        print(f"❌ Connection Error: {e}")
    except json.JSONDecodeError as e:
        print(f"❌ JSON Decode Error: {e}")
    except Exception as e:
        print(f"❌ Unexpected Error: {e}")

def test_flask_status():
    """Test the Flask status endpoint"""
    import requests
    
    print("\n🌐 Testing Flask Status Endpoint...")
    print("-" * 50)
    
    try:
        response = requests.get('http://localhost:10000')
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print("✅ Flask Status Success!")
            print(json.dumps(data, indent=2))
        else:
            print(f"❌ Flask Error: Status {response.status_code}")
            
    except requests.exceptions.ConnectionError:
        print("❌ Flask server is not running on localhost:10000")
    except Exception as e:
        print(f"❌ Unexpected Error: {e}")

if __name__ == "__main__":
    print("🤖 Free Fire Like Bot - API Test")
    print("=" * 50)
    
    # Test API
    asyncio.run(test_api())
    
    # Test Flask status
    test_flask_status()
    
    print("\n✅ Testing completed!")
