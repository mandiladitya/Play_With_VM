a=`sudo docker run -d -P cpython` 
b=`sudo docker port $a | tail -c 6`
c=`curl https://checkip.amazonaws.com`
echo  "ssh root@$c -p $b"
