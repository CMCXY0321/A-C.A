可以对指针进行四种算术运算：++、--、+、-
假设 ptr 是一个指向地址 1000 的整型指针，是一个 32 位的整数
```
ptr++
```
在执行完上述的运算之后，ptr 将指向位置 1004，因为 ptr 每增加一次，它都将指向下一个整数位置，即当前位置往后移 4 个字节