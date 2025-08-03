#!/usr/bin/env python3
"""
Test script for the updated Free Fire Like Bot with region selection
"""

import asyncio
import aiohttp
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

async def test_new_api_format():
    """Test the new API format with different regions"""
    
    api_host = os.getenv('API_HOST', 'https://likexthug.vercel.app')
    api_key = os.getenv('RAPIDAPI_KEY', 'GREAT')
    
    print("🚀 Testing New Free Fire Like Bot API Format")
    print(f"API Host: {api_host}")
    print(f"API Key: {api_key}")
    print("=" * 60)
    
    # Test cases with different regions
    test_cases = [
        ("1901984169", "ind", "Valid Indian UID with India region"),
        ("2537964178", "me", "Valid Middle East UID with ME region"),
        ("1192757057", "me", "Valid Middle East UID with ME region"),
        ("123456789", "ind", "Invalid UID with India region"),
    ]
    
    for uid, region, description in test_cases:
        print(f"\n🧪 Testing: {description}")
        print(f"UID: {uid}, Region: {region}")
        print("-" * 50)
        
        try:
            async with aiohttp.ClientSession() as session:
                url = f"{api_host}/like"
                params = {
                    'uid': uid,
                    'region': region,
                    'key': api_key
                }
                
                print(f"Request: {url}?uid={uid}&region={region}&key={api_key}")
                
                async with session.get(url, params=params) as response:
                    print(f"HTTP Status: {response.status}")
                    
                    if response.status == 200:
                        data = await response.json()
                        api_status = data.get('status', 0)
                        
                        if 'error' in data:
                            print(f"❌ API Error: {data['error']}")
                            print("🔍 Bot will show: Player Not Found")
                        elif api_status in [1, 2]:
                            print(f"✅ Success! API Status: {api_status}")
                            
                            player = data.get('player', {})
                            likes = data.get('likes', {})
                            api_info = data.get('api_key_details', {})
                            
                            print(f"Player: {player.get('nickname', 'N/A')} (Region: {player.get('region', 'N/A')})")
                            print(f"Likes: {likes.get('before', 0)} → {likes.get('after', 0)} (+{likes.get('added_by_api', 0)})")
                            print(f"API Usage: {api_info.get('current_usage', 0)}/{api_info.get('usage_limit', 0)}")
                            print("🔍 Bot will show: Success with likes sent")
                        else:
                            print(f"❌ Unexpected API Status: {api_status}")
                    else:
                        print(f"❌ HTTP Error: {response.status}")
                        print("🔍 Bot will show: Connection Error")
                        
        except Exception as e:
            print(f"❌ Exception: {e}")

if __name__ == "__main__":
    asyncio.run(test_new_api_format())
    
    print("\n" + "=" * 60)
    print("✅ New API format testing completed!")
    print("\nℹ️  New Bot Command Usage:")
    print("• /like <uid> - Uses default region (ind)")
    print("• /like <uid> <region> - Uses specified region")
    print("• Available regions: ind, bg, me, etc.")
    print("\nExample:")
    print("• /like 1901984169 ind - Indian player")
    print("• /like 2537964178 me - Middle East player")
    print("• /like 1192757057 bg - Bangladesh player")
