#!/usr/bin/env python3
"""
Comprehensive test script for Free Fire Like Bot
"""

import asyncio
import aiohttp
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

async def test_uid(uid, description):
    """Test a specific UID with both regions"""
    
    api_host = os.getenv('API_HOST', 'https://likexthug.vercel.app')
    api_key = os.getenv('RAPIDAPI_KEY', 'GREAT')
    
    print(f"\n🧪 Testing {description}")
    print(f"UID: {uid}")
    print("-" * 50)
    
    try:
        async with aiohttp.ClientSession() as session:
            url = f"{api_host}/like"
            
            # Test India region first
            print("🇮🇳 Testing India (ind) region...")
            params = {
                'uid': uid,
                'region': 'ind',
                'key': api_key
            }
            
            async with session.get(url, params=params) as response:
                if response.status == 200:
                    data = await response.json()
                    
                    if 'error' in data:
                        print(f"❌ India region failed: {data['error']}")
                        
                        # Try AG region as fallback
                        print("🌍 Trying AG region as fallback...")
                        params['region'] = 'ag'
                        
                        async with session.get(url, params=params) as fallback_response:
                            if fallback_response.status == 200:
                                fallback_data = await fallback_response.json()
                                
                                if 'error' in fallback_data:
                                    print(f"❌ AG region also failed: {fallback_data['error']}")
                                    print("🔍 Bot will show: Player Not Found")
                                else:
                                    api_status = fallback_data.get('status', 0)
                                    if api_status in [1, 2]:
                                        print(f"✅ AG region success! Status: {api_status}")
                                        player = fallback_data.get('player', {})
                                        likes = fallback_data.get('likes', {})
                                        print(f"Player: {player.get('nickname', 'N/A')} (Region: {player.get('region', 'N/A')})")
                                        print(f"Likes: {likes.get('before', 0)} → {likes.get('after', 0)} (+{likes.get('added_by_api', 0)})")
                                        print("🔍 Bot will show: Success with fallback note")
                                    else:
                                        print(f"❌ AG region unsuccessful status: {api_status}")
                    else:
                        api_status = data.get('status', 0)
                        if api_status in [1, 2]:
                            print(f"✅ India region success! Status: {api_status}")
                            player = data.get('player', {})
                            likes = data.get('likes', {})
                            print(f"Player: {player.get('nickname', 'N/A')} (Region: {player.get('region', 'N/A')})")
                            print(f"Likes: {likes.get('before', 0)} → {likes.get('after', 0)} (+{likes.get('added_by_api', 0)})")
                            print("🔍 Bot will show: Success with India region")
                        else:
                            print(f"❌ India region unsuccessful status: {api_status}")
                else:
                    print(f"❌ HTTP Error: {response.status}")
                    
    except Exception as e:
        print(f"❌ Error: {e}")

async def main():
    print("🤖 Free Fire Like Bot - Comprehensive Test")
    print("=" * 60)
    
    # Test cases
    test_cases = [
        ("1901984169", "Valid Indian UID (should work with ind region)"),
        ("2537964178", "Valid Middle East UID (should work with ag region)"),
        ("1065775237137965127", "Invalid/Non-existent UID (should show player not found)"),
        ("123456789", "Invalid UID format (should show player not found)")
    ]
    
    for uid, description in test_cases:
        await test_uid(uid, description)
    
    print("\n" + "=" * 60)
    print("✅ Comprehensive testing completed!")
    print("\nℹ️  Summary of expected bot behavior:")
    print("• Valid Indian UIDs: Success with India region")
    print("• Valid non-Indian UIDs: Success with AG region + fallback note")
    print("• Invalid UIDs: Clear 'Player Not Found' message")
    print("• Network errors: Connection error message")

if __name__ == "__main__":
    asyncio.run(main())
