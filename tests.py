# from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

def test():
    # result1 = get_files_info("calculator", ".")

    # print(f"Result for current directory:")
    # print(f"{result1}")

    # result2 = get_files_info("calculator", "pkg")

    # print(f"Result for 'pkg' directory:")
    # print(f"{result2}")

    # result3 = get_files_info("calculator", "/bin")

    # print(f"Result for '/bin' directory:")
    # print(f"{result3}")

    # result4 = get_files_info("calculator", "../")

    # print(f"Result for '../' directory:")
    # print(f"{result4}")
    
    result = get_file_content("calculator", "lorem.txt")
    print(f"Result for lorem:")
    print(result)

if __name__ == "__main__":
    test()