#!/usr/bin/env python3
"""
Test script to verify the Free Fire Like Bot with Indian UID
"""

import asyncio
import aiohttp
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

async def test_indian_uid():
    """Test with the specific Indian UID provided by user"""
    
    api_host = os.getenv('API_HOST', 'https://likexthug.vercel.app')
    api_key = os.getenv('RAPIDAPI_KEY', 'GREAT')
    
    print("🇮🇳 Testing Free Fire Like Bot with Indian UID...")
    print(f"API Host: {api_host}")
    print(f"API Key: {api_key}")
    print("-" * 60)
    
    uid = '1901984169'  # Indian UID provided by user
    
    try:
        async with aiohttp.ClientSession() as session:
            url = f"{api_host}/like"
            
            # Test India region
            print(f"🎯 Testing UID: {uid} with India region...")
            params = {
                'uid': uid,
                'region': 'ind',
                'key': api_key
            }
            
            async with session.get(url, params=params) as response:
                print(f"HTTP Status: {response.status}")
                
                if response.status == 200:
                    data = await response.json()
                    api_status = data.get('status', 0)
                    
                    print(f"API Status: {api_status}")
                    print("Raw Response:")
                    print(json.dumps(data, indent=2))
                    
                    if api_status in [1, 2]:
                        print("\n✅ SUCCESS! Indian UID works perfectly!")
                        
                        # Extract key information
                        player = data.get('player', {})
                        likes = data.get('likes', {})
                        api_info = data.get('api_key_details', {})
                        
                        print("\n📊 Success Summary:")
                        print(f"Player UID: {player.get('uid', 'N/A')}")
                        print(f"Player Region: {player.get('region', 'N/A')}")
                        print(f"Player Nickname: {player.get('nickname', 'N/A')}")
                        print(f"Likes Before: {likes.get('before', 0):,}")
                        print(f"Likes After: {likes.get('after', 0):,}")
                        print(f"Likes Added: {likes.get('added_by_api', 0)}")
                        print(f"API Usage: {api_info.get('current_usage', 0)}/{api_info.get('usage_limit', 0)}")
                        
                        print("\n🎉 The bot should now work correctly with Indian UIDs!")
                        
                    else:
                        print(f"\n❌ API returned unsuccessful status: {api_status}")
                        if 'error' in data:
                            print(f"Error message: {data['error']}")
                        
                else:
                    print(f"\n❌ HTTP Error: {response.status}")
                    error_text = await response.text()
                    print(f"Error Response: {error_text}")
                    
    except Exception as e:
        print(f"❌ Unexpected Error: {e}")

if __name__ == "__main__":
    print("🤖 Free Fire Like Bot - Indian UID Test")
    print("=" * 60)
    
    asyncio.run(test_indian_uid())
    
    print("\n✅ Indian UID testing completed!")
