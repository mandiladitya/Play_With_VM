a=`sudo docker run -d -P eg_sshd` 
b=`sudo docker port $a | tail -c 6`
c=`python3 details.py`
echo  "$c -p $b"   
