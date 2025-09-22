# from functions.get_files_info import get_files_info
# from functions.get_file_content import get_file_content
from functions.write_file import write_file

def test():
    # File info tests:
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
    
    
    # File content tests:
    # result = get_file_content("calculator", "lorem.txt")
    # print(f"Result for lorem:")
    # print(result)
    
    # result = get_file_content("calculator", "main.py")
    # print(result)
    
    # result = get_file_content("calculator", "pkg/calculator.py")
    # print(result)
    
    # result = get_file_content("calculator", "/bin/cat")
    # print(result)
    
    # result = get_file_content("calculator", "pkg/does_not_exist.py")
    # print(result)


    # File writing tests:
    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(result)
    
    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(result)
    
    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(result)

if __name__ == "__main__":
    test()