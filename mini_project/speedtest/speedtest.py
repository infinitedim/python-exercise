import speedtest as speedtest

st = speedtest.Speedtest()
st.get_best_server()

print(f"Download: {format(st.download() / 1000000, '.2f')}Mb")
print(f"Upload: {format(st.upload() / 1000000, '.2f')}Mb")
print(f"Ping: {int(st.results.ping)}ms")


