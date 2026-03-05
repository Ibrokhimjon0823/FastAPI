import asyncio


# 1. BUILDING THE BOX
# An async function that just returns a string. No 'await' inside.
async def get_carrot():
    return "Here is a real carrot!"


# 2. USING THE BOX
async def main():
    # print("--- SCENARIO 1: FORGETTING AWAIT ---")
    # # We call it without await. We just get the 'coupon'.
    # bad_result = get_carrot()
    # print("Value:", bad_result)
    # print("Type: ", type(bad_result))

    print("\n--- SCENARIO 2: USING AWAIT ---")
    # We call it WITH await. We cash the coupon for the real thing.
    good_result = await get_carrot()
    print("Value:", good_result)
    print("Type: ", type(good_result))


# This is just how we start an async program in standard Python
if __name__ == "__main__":
    asyncio.run(main())
