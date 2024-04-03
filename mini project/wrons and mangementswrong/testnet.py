import speedtest

def measure_internet_speed():
    st = speedtest.Speedtest()
    st.get_best_server()
    
    download_speed = st.download() / 10**6  # به مگابایت بر ثانیه
    upload_speed = st.upload() / 10**6  # به مگابایت بر ثانیه
    
    print("سرعت دانلود: {:.2f} مگابایت بر ثانیه".format(download_speed))
    print("سرعت آپلود: {:.2f} مگابایت بر ثانیه".format(upload_speed))

if __name__ == "__main__":
    measure_internet_speed()
