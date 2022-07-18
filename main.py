import speedtest
from functools import partial
from time import sleep
from speed_storage import speed_storage

    

def bytes_to_mb(bytes:float) -> float:
    return bytes/(1024*1024)

def print_speeds(down:float,up:int)->None:
    print(f"{'#'*25}")
    print(f"Upload speed: {up:.2f}mb/s")
    print(f"Download speed: {down:.2f}mb/s")
    print(f"{'#'*25}")


def test_speed(speed_tester:speedtest.Speedtest, output_function:partial):
    download_speed = speed_tester.download()
    download_speed = bytes_to_mb(download_speed)

    upload_speed = speed_tester.upload()
    upload_speed = bytes_to_mb(upload_speed)

    output_function(download_speed,upload_speed)

def main():
    file_name = "speedtest_data.csv"
    st = speedtest.Speedtest()
    storage_class = speed_storage(  file_name=file_name,
                                    entries_before_write=5)
                                    
    output_function = partial(storage_class.save_data)
    #output_function=partial(print_speeds)
    print("Starting:")
    while True:
        print(end=".")
        test_speed(speed_tester=st, output_function=output_function)
        sleep(4.5*60)
    print("\nDone!")


if __name__ == "__main__":
    main()