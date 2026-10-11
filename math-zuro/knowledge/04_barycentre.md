# المحور 4: المرجح في المستوي

## 1. التعاريف

### [DEF-BAR-01] النقطة المرجّحة
- النقطة المرجّحة هي زوج $(A,\alpha)$ حيث $A$ نقطة و$\alpha$ عدد حقيقي يسمى **المعامل** (أو الثقل).

### [DEF-BAR-02] المرجح (النقطة المرجحة الناتجة)
- ليكن $(A,\alpha)$ و$(B,\beta)$ نقطتين مرجحتين مع $\alpha+\beta\ne0$.
- المرجح $G$ للمجموعة $\{(A,\alpha),(B,\beta)\}$ هو النقطة التي تحقق:
$$\alpha\,\overrightarrow{GA}+\beta\,\overrightarrow{GB}=\vec 0$$
- نكتب: $G=\operatorname{bar}\{(A,\alpha),(B,\beta)\}$.

### [DEF-BAR-03] المرجح لثلاث نقاط
- ليكن $(A,\alpha),(B,\beta),(C,\gamma)$ مع $\alpha+\beta+\gamma\ne0$.
- $G=\operatorname{bar}\{(A,\alpha),(B,\beta),(C,\gamma)\}$ هي النقطة التي تحقق $\alpha\overrightarrow{GA}+\beta\overrightarrow{GB}+\gamma\overrightarrow{GC}=\vec0$.

---

## 2. الخواص (مبرهنات أساسية)

### [THM-BAR-01] وجود المرجح ووحدانيته
- إذا كان مجموع المعاملات غير معدوم، فإن المرجح موجود ووحيد.
- إذا كان مجموع المعاملات معدوماً، فالمجموع $\alpha\overrightarrow{MA}+\beta\overrightarrow{MB}$ لا يتعلق بالنقطة $M$ (متجه ثابت)، ولا يوجد مرجح بالمعنى السابق.

### [THM-BAR-02] خاصية الاختزال (الأهم)
- إذا كان $G=\operatorname{bar}\{(A,\alpha),(B,\beta)\}$ فإنه من أجل أي نقطة $M$:
$$\alpha\overrightarrow{MA}+\beta\overrightarrow{MB}=(\alpha+\beta)\overrightarrow{MG}$$
- وبالنسبة لثلاث نقاط:
$$\alpha\overrightarrow{MA}+\beta\overrightarrow{MB}+\gamma\overrightarrow{MC}=(\alpha+\beta+\gamma)\overrightarrow{MG}$$

### [THM-BAR-03] التعيين الشعاعي للمرجح
- $G=\operatorname{bar}\{(A,\alpha),(B,\beta)\}$ يكافئ: $\overrightarrow{AG}=\dfrac{\beta}{\alpha+\beta}\overrightarrow{AB}$.
- و$\overrightarrow{BG}=\dfrac{\alpha}{\alpha+\beta}\overrightarrow{BA}$.

### [RULE-BAR-01] خاصية التجميع (الجمعية)
- يمكن استبدال نقطتين مرجحتين بمرجحهما إذا كان مجموع معاملهما غير معدوم:
$$\operatorname{bar}\{(A,\alpha),(B,\beta),(C,\gamma)\}=\operatorname{bar}\{(G_{AB},\alpha+\beta),(C,\gamma)\}$$
حيث $G_{AB}=\operatorname{bar}\{(A,\alpha),(B,\beta)\}$.

### [RULE-BAR-02] خاصية التجانس (الضرب في عدد)
- المرجح لا يتغيّر إذا ضُربت كل المعاملات في عدد $k\ne0$:
$$\operatorname{bar}\{(A,\alpha),(B,\beta)\}=\operatorname{bar}\{(A,k\alpha),(B,k\beta)\}$$

### [RULE-BAR-03] الحالات الخاصة
- إذا كان $\alpha=\beta$ فإن $G$ هو **منتصف** $[AB]$.
- إذا كان $\alpha$ و$\beta$ من **نفس الإشارة** فإن $G$ يقع **داخل** القطعة $[AB]$.
- إذا كان $\alpha$ و$\beta$ من **إشارتين مختلفتين** فإن $G$ يقع **خارج** القطعة $[AB]$، أقرب إلى النقطة التي معاملها الأكبر في القيمة المطلقة.
- إذا كانت $\alpha=\beta=\gamma$ في ثلاث نقاط فإن $G$ هو **مركز ثقل** المثلث.

### [THM-BAR-04] مركز ثقل المثلث
- $G=\operatorname{bar}\{(A,1),(B,1),(C,1)\}$ هو مركز ثقل المثلث $ABC$.
- يتحقق: $\overrightarrow{MA}+\overrightarrow{MB}+\overrightarrow{MC}=3\overrightarrow{MG}$.
- نقطة $G$ تقع على كل **متوسط** من متوسطات المثلث، وتحقق: $AG=\dfrac23AA'$ حيث $A'$ منتصف $[BC]$، وكذلك $BG=\dfrac23BB'$ و$CG=\dfrac23CC'$.

### [THM-BAR-05] تلاقي المتوسطات
- المتوسطات الثلاثة لمثلث متلاقية في نقطة واحدة هي مركز الثقل $G$.

---

## 3. الإحداثيات

### [RULE-BAR-04] إحداثيات المرجح
- إذا كانت $G=\operatorname{bar}\{(A,\alpha),(B,\beta)\}$ فإن:
$$x_G=\dfrac{\alpha x_A+\beta x_B}{\alpha+\beta},\qquad y_G=\dfrac{\alpha y_A+\beta y_B}{\alpha+\beta}$$
- وإذا كانت $G=\operatorname{bar}\{(A,\alpha),(B,\beta),(C,\gamma)\}$:
$$x_G=\dfrac{\alpha x_A+\beta x_B+\gamma x_C}{\alpha+\beta+\gamma},\qquad y_G=\dfrac{\alpha y_A+\beta y_B+\gamma y_C}{\alpha+\beta+\gamma}$$

### [RULE-BAR-05] إحداثيات منتصف قطعة
- منتصف $[AB]$: $\left(\dfrac{x_A+x_B}{2},\ \dfrac{y_A+y_B}{2}\right)$.

---

## 4. تطبيقات (المنهجية)

### [METH-BAR-01] إثبات أن ثلاث نقاط مستقيمية أو أن نقطة تقع على مستقيم
1. **الطريقة المباشرة:** أثبت أن $\overrightarrow{AB}=k\overrightarrow{AC}$ لعدد حقيقي $k$.
2. **بالمرجح:** اكتب النقطة $G$ مرجحاً لنقطتين $A$ و$B$ (مثلاً $G=\operatorname{bar}\{(A,\alpha),(B,\beta)\}$)، فإن $G$ تقع على المستقيم $(AB)$ بالتعريف وبـ[THM-BAR-03].
3. **التحقق:** إذا كانت $G$ تقع على $(AB)$ وعلى $(AC)$ معاً، فإن النقاط $A,B,C$ مستقيمية إذا كانت $G\neq A$.

### [METH-BAR-02] إثبات تلاقي ثلاثة مستقيمات
- أوجد مرجحاً لثلاث نقاط يقع على المستقيمات الثلاثة، فيكون نقطة تلاقيها.

### [METH-BAR-03] إيجاد مجموعة النقاط $M$ بحيث $\|\alpha\overrightarrow{MA}+\beta\overrightarrow{MB}\|=k$
1. استعمل خاصية الاختزال: $\alpha\overrightarrow{MA}+\beta\overrightarrow{MB}=(\alpha+\beta)\overrightarrow{MG}$.
2. إذن: $|\alpha+\beta|\cdot MG=k$، أي $MG=\dfrac{k}{|\alpha+\beta|}$.
3. المجموعة هي **دائرة** مركزها $G$ ونصف قطرها $\dfrac{k}{|\alpha+\beta|}$.
- إذا كان $\alpha+\beta=0$ تصبح العبارة ثابتة، فيكون $\|\vec{AB}\|\cdot|\alpha|=k$ شرطاً لا علاقة له بـ $M$، والمجموعة فارغة أو المستوي كله.

### [METH-BAR-04] إيجاد مجموعة النقاط $M$ بحيث $\alpha MA^2+\beta MB^2=k$
- نستعمل نقطة مرجحة $G$ تحقق الاختزال، ثم نكتب $\alpha MA^2+\beta MB^2=(\alpha+\beta)MG^2+\text{ثابت}$، ثم نحدد المجموعة كدائرة أو نقطة أو فارغة حسب الإشارة.

---

## 5. أمثلة محلولة

### [EX-BAR-01] مرجح نقطتين بالإحداثيات
$A(1,2)$، $B(3,6)$، $G=\operatorname{bar}\{(A,1),(B,3)\}$:
- $x_G=\dfrac{1\cdot1+3\cdot3}{4}=\dfrac{10}{4}=\dfrac52$، $y_G=\dfrac{1\cdot2+3\cdot6}{4}=\dfrac{20}{4}=5$.
- إذن $G\left(\dfrac52,5\right)$.
- تحقق شعاعي: $\overrightarrow{AG}=\left(\dfrac32,3\right)$ و$\dfrac34\overrightarrow{AB}=\dfrac34(2,4)=\left(\dfrac32,3\right)$ ✓.

### [EX-BAR-02] مرجح ثلاث نقاط
$A(0,0)$، $B(4,0)$، $C(0,6)$، المعاملات $1,1,2$:
- المجموع $=4$.
- $x_G=\dfrac{0+4+0}{4}=1$، $y_G=\dfrac{0+0+12}{4}=3$.
- إذن $G(1,3)$.

### [EX-BAR-03] مركز الثقل
مثلث $ABC$ بـ $A(1,1)$، $B(5,1)$، $C(3,7)$:
- $G=\left(\dfrac{1+5+3}{3},\dfrac{1+1+7}{3}\right)=(3,3)$.
- منتصف $[BC]$: $A'\left(4,4\right)$. تحقق: $\overrightarrow{AG}=(2,2)$ و$\dfrac23\overrightarrow{AA'}=\dfrac23(3,3)=(2,2)$ ✓.

### [EX-BAR-04] مجموعة نقاط
$A$ و$B$ نقطتان بحيث $AB=6$. أوجد مجموعة $M$ حيث $\|\overrightarrow{MA}+\overrightarrow{MB}\|=8$:
- $\overrightarrow{MA}+\overrightarrow{MB}=2\overrightarrow{MI}$ حيث $I$ منتصف $[AB]$.
- إذن $2MI=8$، أي $MI=4$.
- المجموعة: دائرة مركزها $I$ ونصف قطرها $4$.

---

## 6. أخطاء شائعة
- نسيان شرط $\alpha+\beta\ne0$ قبل تعريف المرجح.
- الخطأ في إشارة النسبة: $\overrightarrow{AG}=\dfrac{\beta}{\alpha+\beta}\overrightarrow{AB}$ وليس $\dfrac{\alpha}{\alpha+\beta}$.
- الخلط بين $\alpha\overrightarrow{MA}$ وبين $\alpha MA$ (الأولى متجه، والثانية طول).
- عند ثلاث نقاط، نسيان أن المقام هو مجموع المعاملات الثلاثة.
- الخلط بين مركز الثقل ومنتصف الضلع.
