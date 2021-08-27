Quera
سامانه آموزشی
کالج
بانک سؤالات
مسابقات
مگنت (استخدام)
علی قربان‌پور
خانه
کلاس‌ها
ساختمان‌داده‌ها و الگوریتم‌ها
تمرین عملی چهارم
همه مسائل
همه انواع فایل
مسئله	زمان ارسال	ضریب نمره
(تأخیر)	نمره داوری	نمره استاد	نوع فایل	وضعیت	فایل
نمره خام	نمره با تاخیر
موش‌ آزمایشگاهی و توپ‌هایش	۱۵ اردیبهشت ۱۳۹۸ ساعت ۱۶:۵۵	۷۵٪
۱۰۰	۷۵	...	Python 3.8	۷۵	
Quera
محصولات
آموزش برنامه‌نویسی
آگهی‌های استخدام
سؤالات برنامه‌نویسی
مسابقات
کلاس‌ها
پلتفرم استخدامی
منابع
کوئرامگ توسعه‌دهندگان
کوئرامگ شرکت‌ها
اخبار مسابقات و دوره‌ها
ماشین‌حساب حقوق برنامه‌نویسان
آمار‌های دنیای برنامه‌نویسی
عضویت در خبرنامه
رویداد‌ها
کدکاپ
نمایشگاه کار
هکاتون کدآپ
تریس‌وی
با کوئرا
همکاری با ما
تماس با ما
درباره ما
قوانین و مقررات
حمایت از مسابقات
لوگوی ساماندهی
لوگوی ای‌نماد
لوگوی پارس‌پک
ساخته‌شده با افتخار در ایران | ۱۳۹۴ - ۱۴۰۰ 
heap.py | submission id: 2048147

class Max_heap:

    def __init__(self):
        self.arr = [None]


    def bubble_up(self, index):
        if index == 1:
            return
        elif self.arr[index] <= self.arr[index // 2]:
            return
        else:
            self.arr[index], self.arr[index // 2] = self.arr[index // 2], self.arr[index]
            self.bubble_up(index // 2)


    def bubble_down(self, index):
        if 2 * index > self.arr.__len__() - 1:
            return

        if 2 * index == self.arr.__len__() - 1:
            if self.arr[index] < self.arr[2 * index]:
                self.arr[2 * index], self.arr[index] = self.arr[index], self.arr[2 * index]

        elif self.arr[index] < self.arr[2 * index] or self.arr[index] < self.arr[2 * index + 1]:
            if self.arr[2 * index] > self.arr[2 * index + 1]:
                self.arr[2 * index], self.arr[index] =self.arr[index], self.arr[2 * index]
                self.bubble_down(2 * index)
            else:
                self.arr[2 * index + 1], self.arr[index] = self.arr[index], self.arr[2 * index + 1]
                self.bubble_down(2 * index + 1)


    def insert(self, number):
        self.arr.append(number)
        self.bubble_up(self.arr.__len__() - 1)


    def delete_max(self):
        self.arr[1], self.arr[-1] = self.arr[-1], self.arr[1]
        self.arr.pop(-1)
        self.bubble_down(1)


    def build_heap_with_bubble_down(self, arr):
        self.arr = [0] + arr
        for i in range(len(arr) - 1, 0,-1):
            self.bubble_down(i)




    def get_max(self):
        return self.arr[1]


    def __str__(self):
        print(self.arr)




class Min_heap:

    def __init__(self):
        self.arr = [None]


    def bubble_up(self, index):
        if index == 1:
            return
        elif self.arr[index] >= self.arr[index // 2]:
            return
        else:
            self.arr[index], self.arr[index // 2] = self.arr[index // 2], self.arr[index]
            self.bubble_up(index // 2)


    def bubble_down(self, index):
        if 2 * index > self.arr.__len__() - 1:
            return
        if 2 * index == self.arr.__len__() - 1:
            if self.arr[index] > self.arr[2 * index]:
                self.arr[2 * index], self.arr[index] = self.arr[index], self.arr[2 * index]
            else:
                return
        elif self.arr[index] > self.arr[2 * index] or self.arr[index] > self.arr[2 * index + 1]:
            if self.arr[2 * index] < self.arr[2 * index + 1]:
                self.arr[2 * index], self.arr[index] = self.arr[index], self.arr[2 * index]
                self.bubble_down(2 * index)
            else:
                self.arr[2 * index + 1], self.arr[index] = self.arr[index], self.arr[2 * index + 1]
                self.bubble_down(2 * index + 1)


    def build_heap_with_bubble_down(self, arr):
        self.arr = [0] + arr
        for i in range(len(arr) - 1, 0,-1):
            self.bubble_down(i)
    # if 2 * index > self.arr.__len__() - 1:
    #    return
    #
    #
        # if 2 * index > self.arr.__len__() - 1:
        #     return
        # else:
        #     if 2 * index == self.arr.__len__() - 1:
        #         if self.arr[index] > self.arr[2 * index]:
        #             self.arr[2 * index], self.arr[index] = self.arr[index], self.arr[2 * index]
        #         else:
        #             return



    def insert(self, number):
        self.arr.append(number)
        self.bubble_up(self.arr.__len__() - 1)


    def delete_min(self):
        self.arr[1], self.arr[-1] = self.arr[-1], self.arr[1]
        self.arr.pop(-1)
        self.bubble_down(1)


    def get_min(self):
        return self.arr[1]


    def __str__(self):
        print(self.arr)



def gift(a, b):
    if (a + b) % 2 == 0:
        return max(a, b) - min(a, b)
    else:
        return max(a, b) - min(a, b) + 1


###################################################################################################
nk = input().split()
n = int(nk[0])
k = int(nk[1])

balls = input().split()
for i in range(len(balls)):
    balls[i] = int(balls[i])

min_heap = Min_heap()
max_heap = Max_heap()

min_heap.build_heap_with_bubble_down(balls)
max_heap.build_heap_with_bubble_down(balls)

gifts = 0
for i in range(k):
    # max_heap.__str__()
    # min_heap.__str__()
    gifts += gift(min_heap.get_min(), max_heap.get_max())
    a = min_heap.get_min()
    b = max_heap.get_max()
    min_heap.delete_min()
    max_heap.delete_max()

    if (min_heap.get_min() + max_heap.get_max()) % 2 == 0:
        min_heap.insert((a + b) / 2)
        max_heap.insert((a + b) / 2)
        max_heap.insert((a + b) / 2)
    else:
        min_heap.insert((a + b) // 2)
        max_heap.insert((a + b) // 2 + 1)

print(int(gifts))

PythonCopy