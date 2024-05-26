import asyncio
import json
from prisma import Prisma

# Function to insert a new user
async def insert_user(email: str, password: str) -> None:
    try:
        # Instantiate the Prisma client
        prisma = Prisma()
        
        # Connect to the database
        await prisma.connect()
        
        # Insert a new user into the database
        user = await prisma.users.create(
            data={            
                'email': email,
                'password': password,
            }
        )
        print(f'Created user: {json.dumps(user.dict(), indent=2, sort_keys=True)}')
    
    except Exception as e:
        print(e)
    
    finally:
        # Disconnect from the database
        await prisma.disconnect()

# Function to select and print all users
async def select_all_users() -> None:
    try:
        # Instantiate the Prisma client
        prisma = Prisma()
        
        # Connect to the database
        await prisma.connect()
        
        # Select all users from the database
        all_users = await prisma.users.find_many()
        print('All users:')
        for user in all_users:
            print(user)
    
    except Exception as e:
        print(e)
    
    finally:
        # Disconnect from the database
        await prisma.disconnect()

# Main function to run the async functions
async def main() -> None:
    # Insert a new user
    await insert_user('newuser@example.com', 'securepassword')
    
    # Select and print all users
    await select_all_users()

# Run the main async function
if __name__ == '__main__':
    asyncio.run(main())
