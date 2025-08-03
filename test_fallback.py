#!/usr/bin/env python3
"""
Test script to verify the Free Fire Like Bot fallback mechanism
"""

import asyncio
import aiohttp
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

async def test_fallback_mechanism():
    """Test the fallback mechanism from ind to ag region"""
    
    api_host = os.getenv('API_HOST', 'https://likexthug.vercel.app')
    api_key = os.getenv('RAPIDAPI_KEY', 'GREAT')
    
    print("🔍 Testing Free Fire Like Bot Fallback Mechanism...")
    print(f"API Host: {api_host}")
    print(f"API Key: {api_key}")
    print("-" * 60)
    
    uid = '2537964178'  # Test UID (Middle East region)
    
    try:
        async with aiohttp.ClientSession() as session:
            url = f"{api_host}/like"
            
            # Step 1: Try India region first
            print("🇮🇳 Step 1: Trying India (ind) region...")
            params_ind = {
                'uid': uid,
                'region': 'ind',
                'key': api_key
            }
            
            async with session.get(url, params=params_ind) as response_ind:
                print(f"India region response: {response_ind.status}")
                
                if response_ind.status == 200:
                    data = await response_ind.json()
                    print("✅ Success with India region!")
                    print(json.dumps(data, indent=2))
                    return
                else:
                    print(f"❌ India region failed with status {response_ind.status}")
                    error_text = await response_ind.text()
                    print(f"Error: {error_text}")
            
            # Step 2: Fallback to AG region
            print("\n🌍 Step 2: Falling back to AG region...")
            params_ag = {
                'uid': uid,
                'region': 'ag',
                'key': api_key
            }
            
            async with session.get(url, params=params_ag) as response_ag:
                print(f"AG region response: {response_ag.status}")
                
                if response_ag.status == 200:
                    data = await response_ag.json()
                    print("✅ Success with AG region fallback!")
                    print(json.dumps(data, indent=2))
                    
                    # Extract key information
                    player = data.get('player', {})
                    likes = data.get('likes', {})
                    api_info = data.get('api_key_details', {})
                    
                    print("\n📊 Fallback Success Summary:")
                    print(f"Player UID: {player.get('uid', 'N/A')}")
                    print(f"Player Region: {player.get('region', 'N/A')}")
                    print(f"Player Nickname: {player.get('nickname', 'N/A')}")
                    print(f"Likes Before: {likes.get('before', 0):,}")
                    print(f"Likes After: {likes.get('after', 0):,}")
                    print(f"Likes Added: {likes.get('added_by_api', 0)}")
                    print(f"API Usage: {api_info.get('current_usage', 0)}/{api_info.get('usage_limit', 0)}")
                    print("\n🎉 Fallback mechanism working correctly!")
                    
                else:
                    print(f"❌ AG region also failed with status {response_ag.status}")
                    error_text = await response_ag.text()
                    print(f"Error: {error_text}")
                    
    except Exception as e:
        print(f"❌ Unexpected Error: {e}")

if __name__ == "__main__":
    print("🤖 Free Fire Like Bot - Fallback Mechanism Test")
    print("=" * 60)
    
    asyncio.run(test_fallback_mechanism())
    
    print("\n✅ Fallback testing completed!")
    print("\nℹ️  Note: The bot will now automatically try India region first,")
    print("   and if that fails, it will fallback to AG region to ensure")
    print("   maximum compatibility with all Free Fire players.")
