# المحور 6: الزوايا الموجهة والحساب المثلثي

## 1. قياس الزوايا

### [DEF-ANG-01] الراديان
- وحدة قياس الزوايا المعتمدة في البرنامج هي **الراديان**.
- الزاوية المستقيمة (أي $\pi$ راديان) $=180^\circ$. إذن: $\text{درجات}\cdot\dfrac{\pi}{180}=\text{راديان}$.
- جدول تحويل شائع: $30^\circ=\dfrac\pi6$، $45^\circ=\dfrac\pi4$، $60^\circ=\dfrac\pi3$، $90^\circ=\dfrac\pi2$، $180^\circ=\pi$، $360^\circ=2\pi$.

### [DEF-ANG-02] الزاوية الموجهة لشعاعين غير معدومين
- الزاوية الموجهة $(\vec u,\vec v)$ هي الدوران الذي يحوّل الشعاع $\vec u$ إلى الشعاع $\vec v$ (في الاتجاه الموجب: عكس عقارب الساعة).
- **قيس** الزاوية $(\vec u,\vec v)$ هو عدد $\theta$ بحيث $\dfrac{\vec u}{\|\vec u\|}$ مدور بزاوية $\theta$ يعطي $\dfrac{\vec v}{\|\vec v\|}$.
- القيس معرّف بالتقريب بـ $2\pi$: نكتب $(\vec u,\vec v)\equiv\theta\ [2\pi]$.
- **القيس الرئيسي:** القيس الوحيد الموجود في المجال $]-\pi,\pi]$.

### [RULE-ANG-01] خواص الزوايا الموجهة
- **علاقة شال:** $(\vec u,\vec v)+(\vec v,\vec w)\equiv(\vec u,\vec w)\ [2\pi]$.
- $(\vec v,\vec u)\equiv-(\vec u,\vec v)\ [2\pi]$.
- $(-\vec u,\vec v)\equiv(\vec u,\vec v)+\pi\ [2\pi]$.
- $(k\vec u,\vec v)\equiv(\vec u,\vec v)\ [2\pi]$ إذا كان $k>0$، و$\equiv(\vec u,\vec v)+\pi\ [2\pi]$ إذا كان $k<0$.

### [RULE-ANG-02] الأشعة والمستقيمات المتوازية وعلاقتها بالزوايا
- $\vec u$ و$\vec v$ مرتبطان خطياً (أي متوازيان) إذا وفقط إذا كان $(\vec u,\vec v)\equiv0\ [\pi]$.
- ثلاث نقاط $A,B,C$ مستقيمية إذا وفقط إذا كان $(\overrightarrow{AB},\overrightarrow{AC})\equiv0\ [\pi]$.

---

## 2. الزاوية المحيطية (مبرهنة هامة)

### [THM-ANG-01] مبرهنة الزاوية المحيطية
- ليكن $O$ مركز دائرة و$A,B$ نقطتان منها، و$M$ نقطة أخرى من الدائرة (مختلفة عن $A$ و$B$).
- **الزاوية المركزية:** $(\overrightarrow{OA},\overrightarrow{OB})\equiv2(\overrightarrow{MA},\overrightarrow{MB})\ [2\pi]$.
- **النتيجة:** الزاوية المحيطية تساوي نصف الزاوية المركزية المرتكزة على القوس نفسه.

### [THM-ANG-02] زوايا محيطية متساوية
- إذا كانت $M,N$ نقطتين من الدائرة نفسها (مختلفتين عن $A,B$) فإن: $(\overrightarrow{MA},\overrightarrow{MB})\equiv(\overrightarrow{NA},\overrightarrow{NB})\ [\pi]$.

### [THM-ANG-03] شرط تواجد أربع نقاط على دائرة واحدة
- النقاط $A,B,C,D$ (متمايزة مثنى مثنى، وليست $C,D$ على $(AB)$) تقع على دائرة واحدة إذا وفقط إذا كان: $(\overrightarrow{CA},\overrightarrow{CB})\equiv(\overrightarrow{DA},\overrightarrow{DB})\ [\pi]$.

---

## 3. الحساب المثلثي (على الدائرة المثلثية)

### [DEF-TRG-01] الدائرة المثلثية
- دائرة مركزها $O$ ونصف قطرها $1$. النقطة $M$ التي قيسها $\theta$ لها إحداثيات: $M(\cos\theta,\ \sin\theta)$.
- $\cos\theta$ هي الفاصلة و$\sin\theta$ هي الترتيبة.
- $\tan\theta=\dfrac{\sin\theta}{\cos\theta}$ مع $\cos\theta\ne0$.

### [RULE-TRG-01] جدول الزوايا الشهيرة (يجب حفظه)
| $\theta$ | $0$ | $\dfrac\pi6$ | $\dfrac\pi4$ | $\dfrac\pi3$ | $\dfrac\pi2$ | $\pi$ |
|---|---|---|---|---|---|---|
| $\cos\theta$ | $1$ | $\dfrac{\sqrt3}2$ | $\dfrac{\sqrt2}2$ | $\dfrac12$ | $0$ | $-1$ |
| $\sin\theta$ | $0$ | $\dfrac12$ | $\dfrac{\sqrt2}2$ | $\dfrac{\sqrt3}2$ | $1$ | $0$ |
| $\tan\theta$ | $0$ | $\dfrac{\sqrt3}3$ | $1$ | $\sqrt3$ | غير معرفة | $0$ |

### [RULE-TRG-02] العلاقات الأساسية
- $\cos^2\theta+\sin^2\theta=1$.
- $-1\le\cos\theta\le1$ و$-1\le\sin\theta\le1$.
- $\tan^2\theta+1=\dfrac{1}{\cos^2\theta}$.

### [RULE-TRG-03] الزوايا المرتبطة (يجب حفظها)
- $\cos(-\theta)=\cos\theta$ و$\sin(-\theta)=-\sin\theta$.
- $\cos(\pi-\theta)=-\cos\theta$ و$\sin(\pi-\theta)=\sin\theta$.
- $\cos(\pi+\theta)=-\cos\theta$ و$\sin(\pi+\theta)=-\sin\theta$.
- $\cos\!\left(\dfrac\pi2-\theta\right)=\sin\theta$ و$\sin\!\left(\dfrac\pi2-\theta\right)=\cos\theta$.
- الدوال $\cos$ و$\sin$ دوريتان دورهما $2\pi$، وأما $\tan$ فدورها $\pi$.

---

## 4. حل المعادلات المثلثية

### [THM-TRG-01] حل $\cos x=\cos a$
$$\cos x=\cos a\iff x=a+2k\pi\quad\text{أو}\quad x=-a+2k\pi,\quad k\in\mathbb Z$$

### [THM-TRG-02] حل $\sin x=\sin a$
$$\sin x=\sin a\iff x=a+2k\pi\quad\text{أو}\quad x=\pi-a+2k\pi,\quad k\in\mathbb Z$$

### [THM-TRG-03] حل $\tan x=\tan a$
$$\tan x=\tan a\iff x=a+k\pi,\quad k\in\mathbb Z$$
(مع $x$ و$a$ يحققان $\cos\ne0$.)

### [METH-TRG-01] منهجية حل معادلة مثلثية
1. اكتب المعادلة على شكل $\cos(\cdot)=\cos(\cdot)$ أو $\sin(\cdot)=\sin(\cdot)$ بالتعويض عن الزاوية الشهيرة المناسبة.
2. طبّق [THM-TRG-01] أو [THM-TRG-02] أو [THM-TRG-03].
3. إذا طُلب حل في مجال معيّن، عوّض قيم $k\in\mathbb Z$ المناسبة وحدد الحلول داخل المجال.

### [EX-TRG-01] حل $\sin(2x)=\dfrac{\sqrt3}{2}$ في $\mathbb{R}$
- $\dfrac{\sqrt3}2=\sin\dfrac\pi3$، إذن: $\sin 2x=\sin\dfrac\pi3$.
- الحالة 1: $2x=\dfrac\pi3+2k\pi$، أي $x=\dfrac\pi6+k\pi$.
- الحالة 2: $2x=\pi-\dfrac\pi3+2k\pi=\dfrac{2\pi}3+2k\pi$، أي $x=\dfrac\pi3+k\pi$.
- مجموعة الحلول: $S=\left\{\dfrac\pi6+k\pi\right\}\cup\left\{\dfrac\pi3+k\pi\right\}$، $k\in\mathbb Z$.

### [EX-TRG-02] حل $2\cos x-\sqrt3=0$ في $[0,2\pi[$
- $\cos x=\dfrac{\sqrt3}2=\cos\dfrac\pi6$.
- $x=\dfrac\pi6+2k\pi$ أو $x=-\dfrac\pi6+2k\pi$.
- في $[0,2\pi[$: $x=\dfrac\pi6$ أو $x=\dfrac{11\pi}6$.

---

## 5. حل المتراجحات المثلثية (بالدائرة المثلثية)

### [METH-TRG-02] منهجية حل متراجحة مثلثية
1. ارسم الدائرة المثلثية وعيّن نقط الحدود (حلول المعادلة المرافقة).
2. استعمل محور الفواصل لـ $\cos$ ومحور التراتيب لـ $\sin$:
   - $\cos x>c$: النقط التي فاصلتها أكبر من $c$ (قوس حول $0$).
   - $\sin x>c$: النقط التي ترتيبها أكبر من $c$ (قوس فوق محور الفواصل).
3. اكتب مجموعة الحلول بالأقواس.

### [EX-TRG-03] حل $2\sin x-1>0$ في $[0,2\pi[$
- $\sin x>\dfrac12$ ⟺ $x\in\left]\dfrac\pi6,\dfrac{5\pi}6\right[$.
- إذن $S=\left]\dfrac\pi6,\dfrac{5\pi}6\right[$.

---

## 6. أمثلة أخرى

### [EX-ANG-01] قيس زاوية موجهة
- $\vec u=(1,0)$ و$\vec v=(0,1)$: $(\vec u,\vec v)\equiv\dfrac\pi2\ [2\pi]$.
- $(\vec v,\vec u)\equiv-\dfrac\pi2\ [2\pi]$ حسب [RULE-ANG-01].

### [EX-ANG-02] التحقق من ثلاث نقاط مستقيمية
- $A(0,0)$ و$B(1,2)$ و$C(2,4)$: $\overrightarrow{AB}=(1,2)$ و$\overrightarrow{AC}=(2,4)=2\overrightarrow{AB}$. إذن $(\overrightarrow{AB},\overrightarrow{AC})\equiv0\ [\pi]$، والنقاط مستقيمية ✓.

---

## 7. أخطاء شائعة
- الخلط بين الدرجات والراديان في الآلة الحاسبة.
- نسيان "$+2k\pi$" أو "$+k\pi$" في الحل العام.
- في المعادلة $\sin x=\sin a$، نسيان الحل الثاني $\pi-a$.
- في المتراجحات، الخلط بين الزاوية المعطاة و"الزاوية المقابلة".
- كتابة $\cos^2x=\cos x^2$ (الصواب: $\cos^2 x=(\cos x)^2$).
- قيمة $\tan\dfrac\pi2$ غير معرفة وليست صفراً.
