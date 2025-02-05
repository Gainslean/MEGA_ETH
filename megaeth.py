import asyncio

from aiohttp import ClientSession

result = []
async def info(wallet):

    url = f"https://nft.megaeth.com/api/whitelist?address={wallet}"
    async with ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                print(data)
                if data["isWhitelisted"] == True:
                    print(f"Кошелек {wallet} прошел")
                    result.append(wallet)


async def main():
    task = []
    with open("wallet.txt", 'r') as f:
        koshi = [line.strip() for line in f.readlines()]

    for wallet in koshi:
        task.append(info(wallet))

    await asyncio.gather(*task)

asyncio.run(main())

print()

print(f"Кошельки которые прошли {result}")