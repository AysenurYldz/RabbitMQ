
# RabbitMQ
Python ile publisher olarak mesaj gönderme ve gelen mesajı consumer olarak alma işlemleri.

## RabbitMQ Kurulumu

RabbitMQ, Erlang programlama dilinde geliştirilmiştir. Bu nedenle RabbitMQ kurulurken ilk adım olarak Erlang programlama dili için kurulum yapılır. Ardından RabbitMQ kurulur.

İlk olarak https://www.erlang.org/downloads adresinden indirilen exe dosyası ile Erlang kurulumu yapılır.

Erlang kurulumu tamamlandıktan sonra https://www.rabbitmq.com/docs/download adresinden bilgisayara uygun olarak RabbitMQ kurulumu yapılır.

## RabbitMQ Konfigürasyon
Konfigürasyon işlemi için Windows tuşuna basıp arama kısmına “RabbitMQ Command Prompt” yazarak arama yapılır.

RabbitMQ Command Prompt’a tıklanır ve aşağıdaki ekran elde edilir:


RabbitMQ kurulumlarından sonra RabbitMQ Plugin-Servisini aktif etmek için komut satırı dizesine alttaki komutu yazalım ve Servis-Plugin’i aktifleştirilmiş olur.

sh
Kodu kopyala
rabbitmq-plugins enable rabbitmq_management

Kurulum ve konfigürasyon işlemlerini tamamladıktan sonra RabbitMQ için browser’a 15672 portundan erişilebilir.

http://localhost:15672


Karşımıza local makinemize kurmuş olduğumuz RabbitMQ login ekranı gelecektir. RabbitMQ kurulumunda varsayılan olarak kullanıcı adı ve şifre tanımlanmış olarak gelir.

yaml
Kodu kopyala
UserName: guest
Password : guest
Python ile İlk Kullanım Örneği
Python ile publisher olarak mesaj göndermek ve gelen mesajı consumer olarak almak için gereken kodlar ve adım adım yapılması gerekenler aşağıda görseller ile açıklanmıştır.

İlk olarak producer.py ve consumer.py olarak adlandırılan publisher ve consumer için python kodu yazılır.

Producer olarak mesaj yazılmasını sağlayan Python kodu (producer.py)
python
Kodu kopyala
import pika

# Bağlantıyı kur
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Kuyruğu oluştur
channel.queue_declare(queue='hello')

# Mesajı gönder
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")

# Bağlantıyı kapat
connection.close()
Consumer olarak mesajın alındığı Python kodu (consumer.py)
python
Kodu kopyala
import pika

# Bağlantıyı kur
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Kuyruğu oluştur
channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

# Mesajları al
channel.basic_consume(queue='hello',
                      on_message_callback=callback,
                      auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
http://localhost:15672 adresine gidilerek RabbitMQ Management’a giriş yapılır. Varsayılan olarak kullanıcı adı ve şifre guest şeklindedir.


Python kodları yazıldıktan sonra kullanılan IDE’ye ait terminal ya da bilgisayarın komut istemi kullanılarak producer.py içerisine yazılan producer kodu çalıştırılır.

sh
Kodu kopyala
python producer.py

Producer.py kodu çalıştırıldıktan sonra RabbitMQ Management’te elde edilen çıktı aşağıdaki gibidir:


Bu işlemlerin ardından consumer.py kodu çalıştırılır.

sh
Kodu kopyala
python consumer.py

Consume işleminden sonra RabbitMQ Management görünümü aşağıdaki gibidir:
