Разработал систему слепой подписи алгоритмом RSA. Программа моделирует слепую подпись 
сообщения "m". Сначала создаются ключи шифрования открытый "openKey" и 
закрытый "closeKey". Далее генерируется ослепляющий множитель r с помощью которого 
маскируется (ослепляется) сообщение "m". Сообщение "m" шифруется с помощью открытого
ключа и ослепляющего множителя и получается зашифрованное сообщение. Далее оно передается
подписывающей стороне, которая с помощью закрытого ключа подписывает сообщение.
Далее сообщение принимается отправителем и демаскируется, после программа получает 
исходное сообщение с помощью открытого ключа и может сравнить его с отправленным, 
если они совпадают, то подписанное сообщение корректно.
Eng(auto)
He developed a blind signature system using the RSA algorithm. The program simulates the blind signature
of the message "m". First, the encryption keys are created public "OpenKey" and
private "closeKey". Next, a blinding multiplier r is generated with which
the message "m" is masked (blinded). The message "m" is encrypted using a public
key and a blinding multiplier and an encrypted message is obtained. Then it is transmitted
to the signing party, which uses the private key to sign the message.
Next, the message is received by the sender and unmasked, after which the program receives 
the original message is using the public key and can compare it with the sent one,
if they match, then the signed message is correct.
