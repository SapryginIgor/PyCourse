import asyncio
import argparse
import aiofiles
import aiohttp
import os

async def write_photo(path, photo_bytes):
    async with aiofiles.open(path, 'wb') as file:
        await file.write(photo_bytes)

async def get_photo(image_name, output_folder, session):
    print(f"{image_name=}")
    url = "https://picsum.photos/200/300.jpg"
    response = await session.get(url)
    photo = await response.read()
    os.makedirs(output_folder, exist_ok=True)
    path = os.path.join(output_folder, image_name)
    await write_photo(path, photo)



async def main(num_photos, output_folder):
    headers = {
        "User-Agent": "Mozilla/5.0",
    }
    async with aiohttp.ClientSession(headers=headers) as session:
        photos = await asyncio.gather(
            *(get_photo(f"image_{i + 1}.jpg", output_folder, session) for i in range(num_photos))
        )
        print("All photos have been downloaded!!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("num_photos", type=int, help="A number of photos to download")
    parser.add_argument("output_folder", type=str, help="Path to the output folder")

    args = parser.parse_args()
    num_photos = args.num_photos
    output_folder = args.output_folder

    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main(num_photos, output_folder))
    finally:
        loop.close()
        # pass