docker stop -beijingsubway \
; docker rm beijing-subway \
; cd /app/beijing-subway \
&& sudo git pull \
&& docker build -t beijing-subway . \
&& docker run -e TZ="Asia/Shanghai" -d -p 16111:3000 --name beijing-subway beijing-subway
