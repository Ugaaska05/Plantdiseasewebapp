#!/usr/bin/env python3
"""
Test Supabase Connection
Run this to verify backend can connect to Supabase
"""

from supabase import create_client, Client
import sys

# Your Supabase credentials
SUPABASE_URL = "https://pqeghyztlzfhphfkzekb.supabase.co"
SUPABASE_SERVICE_ROLE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBxZWdoeXp0bHpmaHBoZmt6ZWtiIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1MzMxMjAzMCwiZXhwIjoyMDY4ODg4MDMwfQ.kOQRqrU5xWNJJkFSGGD_gxV6VC6-xHGA3zmykx8v_0s"

def test_connection():
    try:
        print("🔄 Testing Supabase connection...")
        
        # Create Supabase client
        supabase: Client = create_client(SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY)
        
        # Test connection by querying users table
        result = supabase.table('users').select('id, email, name, role').execute()
        
        print("✅ Connection successful!")
        print(f"📊 Found {len(result.data)} users in database")
        
        # Show users
        for user in result.data:
            print(f"   - {user['name']} ({user['email']}) - {user['role']}")
            
        return True
        
    except Exception as e:
        print(f"❌ Connection failed: {str(e)}")
        return False

if __name__ == "__main__":
    success = test_connection()
    sys.exit(0 if success else 1)