a=`sudo docker run -d -P unodejs2` 
b=`sudo docker port $a | tail -c 6`

c=`curl https://checkip.amazonaws.com`
echo  "ssh root@$c -p $b" 
