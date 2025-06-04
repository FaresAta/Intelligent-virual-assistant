DS_prerequisites = {
    # السنة الأولى
    "Calculus 1": [],
    "التفاضل والتكامل 1": [],

    "Discrete Mathematics": [],
    "الرياضيات المتقطعة": [],

    "Statistics": [],
    "الإحصاء": [],

    "Computer 99": [],
    "مقدمة في الحاسوب": [],

    "Principles of Data Science": [],
    "مبادئ علم البيانات": [],

    "Fundamentals": [],
    "أساسيات الحوسبة": [],

    # السنة الثانية
    "C++": ["Computer 99"],
    "سي بلس بلس": ["مقدمة في الحاسوب"],

    "Linear Algebra": ["Calculus 1"],
    "الجبر الخطي": ["التفاضل والتكامل 1"],

    "OOP": ["Computer 99", "C++"],
    "البرمجة الكائنية": ["مقدمة في الحاسوب", "سي بلس بلس"],

    "Data Engineering": ["Principles of Data Science"],
    "هندسة البيانات": ["مبادئ علم البيانات"],

    "Applied Statistics": ["Statistics"],
    "الإحصاء التطبيقي": ["الإحصاء"],

    "AI Programming": ["Computer 99", "C++"],
    "برمجة الذكاء الاصطناعي": ["مقدمة في الحاسوب", "سي بلس بلس"],

    "Database": ["Computer 99", "C++", "OOP"],
    "قواعد البيانات": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية"],

    "Data Structures": ["Computer 99", "C++", "OOP"],
    "هياكل البيانات": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية"],

    "Data Mining": ["Computer 99", "C++", "OOP", "Database"],
    "تنقيب البيانات": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "قواعد البيانات"],

    "Algorithms": ["Computer 99", "C++", "OOP", "Data Structures"],
    "الخوارزميات": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "هياكل البيانات"],

    # السنة الثالثة
    "Ethics AI & DS": ["Principles of Data Science"],
    "أخلاقيات الذكاء الاصطناعي وعلم البيانات": ["مبادئ علم البيانات"],

    "Seminar": [],
    "ندوة": [],

    "Networks": ["Computer 99", "C++", "OOP"],
    "الشبكات": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية"],

    "Information Security": ["Computer 99", "C++", "OOP", "Database", "Networks"],
    "أمن المعلومات": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "قواعد البيانات", "الشبكات"],

    "Unstructured Database": ["Computer 99", "C++", "OOP", "Database"],
    "قواعد البيانات غير المنظمة": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "قواعد البيانات"],

    "Software": ["Computer 99", "C++", "OOP", "Database"],
    "هندسة البرمجيات": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "قواعد البيانات"],

    "Pattern & Analysis": ["Computer 99", "C++", "OOP", "Database", "Data Mining"],
    "تحليل الأنماط": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "قواعد البيانات", "تنقيب البيانات"],

    "Machine Learning": ["Computer 99", "C++", "OOP", "Database", "Data Mining"],
    "تعلم الآلة": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "قواعد البيانات", "تنقيب البيانات"],

    "AI": ["Computer 99", "C++", "OOP", "Data Structures"],
    "الذكاء الاصطناعي": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "هياكل البيانات"],

    # السنة الرابعة
    "Cloud Computing": ["Computer 99", "C++", "OOP", "Networks"],
    "الحوسبة السحابية": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "الشبكات"],

    "Big Data": ["Computer 99", "C++", "OOP", "Networks", "Cloud Computing"],
    "البيانات الضخمة": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "الشبكات", "الحوسبة السحابية"],

    "Deep Learning": ["Computer 99", "C++", "OOP", "Database", "Data Mining", "Machine Learning"],
    "التعلم العميق": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "قواعد البيانات", "تنقيب البيانات", "تعلم الآلة"],

    "Form Publishing": ["Computer 99", "C++", "OOP", "Database", "Data Mining", "Machine Learning"],
    "نشر النماذج": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "قواعد البيانات", "تنقيب البيانات", "تعلم الآلة"],

    "Data Visualization": ["Computer 99", "C++", "OOP", "Database", "Data Mining", "Machine Learning"],
    "تصور البيانات": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "قواعد البيانات", "تنقيب البيانات", "تعلم الآلة"],

    "NLP": ["Computer 99", "C++", "OOP", "Data Structures", "AI"],
    "معالجة اللغة الطبيعية": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "هياكل البيانات", "الذكاء الاصطناعي"],

    "Graduation Project 1": ["Passed 90 Credit Hours"],
    "مشروع التخرج 1": ["اجتياز 90 ساعة معتمدة"],

    "Graduation Project 2": ["Graduation Project 1"],
    "مشروع التخرج 2": ["مشروع التخرج 1"],

    "Training": ["Passed 90 Credit Hours"],
    "التدريب": ["اجتياز 90 ساعة معتمدة"]
}





AI_prerequisites = {
    # السنة الأولى
    "Fundamentals": [],
    "أساسيات الحوسبة": [],

    "Computer 99": [],
    "مقدمة في الحاسوب": [],

    "C++": ["Computer 99"],
    "سي بلس بلس": ["مقدمة في الحاسوب"],

    "Discrete": [],
    "الرياضيات المتقطعة": [],

    "Linear Algebra": ["Calculus 1"],
    "الجبر الخطي": ["التفاضل والتكامل 1"],

    "Calculus 1": [],
    "التفاضل والتكامل 1": [],

    "Intro to AI": ["Fundamentals"],
    "مقدمة في الذكاء الاصطناعي": ["أساسيات الحوسبة"],

    "AI Programming": ["Computer 99", "C++"],
    "برمجة الذكاء الاصطناعي": ["مقدمة في الحاسوب", "سي بلس بلس"],

    "OOP": ["Computer 99", "C++"],
    "البرمجة الكائنية": ["مقدمة في الحاسوب", "سي بلس بلس"],

    "Web": ["Computer 99", "C++"],
    "تطوير تطبيقات الويب": ["مقدمة في الحاسوب", "سي بلس بلس"],

    # السنة الثانية
    "Ethics AI & DS": ["Intro to AI", "Fundamentals"],
    "أخلاقيات الذكاء الاصطناعي وعلم البيانات": ["مقدمة في الذكاء الاصطناعي", "أساسيات الحوسبة"],

    "Knowledge & Reasoning": ["Intro to AI", "Fundamentals"],
    "تمثيل واستخراج المعرفة": ["مقدمة في الذكاء الاصطناعي", "أساسيات الحوسبة"],

    "Database": ["Computer 99", "C++", "OOP"],
    "قواعد البيانات": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية"],

    "Data Structures": ["Computer 99", "C++", "OOP"],
    "هياكل البيانات": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية"],

    "Data Mining": ["Computer 99", "C++", "OOP", "Database"],
    "تنقيب البيانات": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "قواعد البيانات"],

    "Algorithm": ["Computer 99", "C++", "OOP", "Data Structures"],
    "الخوارزميات": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "هياكل البيانات"],

    "AI": ["Computer 99", "C++", "OOP", "Data Structures"],
    "الذكاء الاصطناعي": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "هياكل البيانات"],

    "Machine Learning": ["Computer 99", "C++", "OOP", "Database", "Data Mining"],
    "تعلم الآلة": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "قواعد البيانات", "تنقيب البيانات"],

    "Statistics": [],
    "الإحصاء": [],

    # السنة الثالثة
    "Seminar": [],
    "ندوة": [],

    "HCI": ["Computer 99", "C++", "Web"],
    "التفاعل بين الإنسان والحاسوب": ["مقدمة في الحاسوب", "سي بلس بلس", "تطوير تطبيقات الويب"],

    "Networks": ["Computer 99", "C++", "OOP"],
    "الشبكات": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية"],

    "Embedded System": ["Computer 99", "C++", "OOP", "Data Structures"],
    "الأنظمة المدمجة": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "هياكل البيانات"],

    "Ontologies": ["Fundamentals", "Intro to AI", "Knowledge & Reasoning"],
    "الأنطولوجيا والتمثيل المعرفي": ["أساسيات الحوسبة", "مقدمة في الذكاء الاصطناعي", "تمثيل واستخراج المعرفة"],

    "Info Security": ["Computer 99", "C++", "OOP", "Database or Networks"],
    "أمن المعلومات": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "قواعد البيانات أو الشبكات"],

    "Software": ["Computer 99", "C++", "OOP", "Database"],
    "هندسة البرمجيات": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "قواعد البيانات"],

    "NLP": ["Computer 99", "C++", "OOP", "Data Structures", "AI"],
    "معالجة اللغة الطبيعية": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "هياكل البيانات", "الذكاء الاصطناعي"],

    "Computer Vision": ["Computer 99", "C++", "OOP", "Database", "Data Mining", "Machine Learning"],
    "الرؤية الحاسوبية": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "قواعد البيانات", "تنقيب البيانات", "تعلم الآلة"],

    # السنة الرابعة
    "Robotics": ["Computer 99", "C++", "OOP", "Data Structures", "Embedded System"],
    "الروبوتات الذكية": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "هياكل البيانات", "الأنظمة المدمجة"],

    "Cognitive": ["Computer 99", "C++", "OOP", "Data Structures", "AI"],
    "علوم الإدراك": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "هياكل البيانات", "الذكاء الاصطناعي"],

    "IOT": ["Computer 99", "C++", "OOP", "Networks"],
    "إنترنت الأشياء": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "الشبكات"],

    "Deep Learning": ["Computer 99", "C++", "OOP", "Database", "Data Mining", "Machine Learning"],
    "التعلم العميق": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "قواعد البيانات", "تنقيب البيانات", "تعلم الآلة"],

    "Graduation Project 1": ["Passed 90 Credit Hours"],
    "مشروع التخرج 1": ["اجتياز 90 ساعة معتمدة"],

    "Graduation Project 2": ["Graduation Project 1"],
    "مشروع التخرج 2": ["مشروع التخرج 1"],

    "Training": ["Passed 90 Credit Hours"],
    "التدريب": ["اجتياز 90 ساعة معتمدة"]
}





CS_prerequisites = {
    # السنة الأولى
    "Calculus 1": [],
    "التفاضل والتكامل 1": [],

    "Fundamentals": [],
    "أساسيات الحوسبة": [],

    "Computer 99": [],
    "مقدمة في الحاسوب": [],

    "Discrete": [],
    "الرياضيات المتقطعة": [],

    "Physics": [],
    "الفيزياء": [],

    "Linear CS": ["Calculus 1"],
    "الجبر الخطي لعلوم الحاسوب": ["التفاضل والتكامل 1"],

    "C++": ["Computer 99"],
    "سي بلس بلس": ["مقدمة في الحاسوب"],

    "Web": ["Computer 99", "C++"],
    "تصميم الويب": ["مقدمة في الحاسوب", "سي بلس بلس"],

    "OOP": ["Computer 99", "C++"],
    "البرمجة الكائنية": ["مقدمة في الحاسوب", "سي بلس بلس"],

    # السنة الثانية
    "Calculus 2": ["Calculus 1"],
    "التفاضل والتكامل 2": ["التفاضل والتكامل 1"],

    "Numerical": ["Calculus 1", "Linear CS"],
    "التحليل العددي": ["التفاضل والتكامل 1", "الجبر الخطي لعلوم الحاسوب"],

    "Theory": ["Discrete"],
    "نظرية الحوسبة": ["الرياضيات المتقطعة"],

    "Logic": ["Discrete"],
    "المنطق الرياضي": ["الرياضيات المتقطعة"],

    "Statistics": [],
    "الإحصاء": [],

    "Database": ["Computer 99", "C++", "OOP"],
    "قواعد البيانات": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية"],

    "Data Structures": ["Computer 99", "C++", "OOP"],
    "هياكل البيانات": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية"],

    "Advanced Programming": ["Computer 99", "C++", "OOP", "Data Structures"],
    "البرمجة المتقدمة": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "هياكل البيانات"],

    # السنة الثالثة
    "Seminar": [],
    "ندوة": [],

    "Organization": ["Discrete", "Logic"],
    "تنظيم الحاسوب": ["الرياضيات المتقطعة", "المنطق الرياضي"],

    "Simulation": ["Statistics"],
    "المحاكاة": ["الإحصاء"],

    "Networks": ["Computer 99", "C++", "OOP"],
    "الشبكات": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية"],

    "Software": ["Computer 99", "C++", "OOP", "Database"],
    "هندسة البرمجيات": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "قواعد البيانات"],

    "Graphics": ["Computer 99", "C++", "OOP", "Data Structures"],
    "الرسوميات الحاسوبية": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "هياكل البيانات"],

    "Algorithms": ["Computer 99", "C++", "OOP", "Data Structures"],
    "الخوارزميات": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "هياكل البيانات"],

    "Ethics": ["Computer 99", "C++", "OOP", "Database", "Software"],
    "أخلاقيات الحوسبة": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "قواعد البيانات", "هندسة البرمجيات"],

    "AI": ["Computer 99", "C++", "OOP", "Data Structures"],
    "الذكاء الاصطناعي": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "هياكل البيانات"],

    # السنة الرابعة
    "PL": ["Theory", "Discrete"],
    "لغات البرمجة": ["نظرية الحوسبة", "الرياضيات المتقطعة"],

    "Compiler": ["Theory", "Discrete"],
    "المترجمات": ["نظرية الحوسبة", "الرياضيات المتقطعة"],

    "Security": ["Computer 99", "C++", "OOP", "Database"],
    "أمن المعلومات": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "قواعد البيانات"],

    "Parallel": ["Discrete", "Logic", "Organization"],
    "الحوسبة المتوازية": ["الرياضيات المتقطعة", "المنطق الرياضي", "تنظيم الحاسوب"],

    "Computational Problem": ["Computer 99", "C++", "OOP", "Data Structures", "Algorithms"],
    "المشاكل الحاسوبية": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "هياكل البيانات", "الخوارزميات"],

    "OS": ["Computer 99", "C++", "OOP", "Data Structures"],
    "أنظمة التشغيل": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "هياكل البيانات"],

    "Graduation Project 1": ["Passed 90 Credit Hours"],
    "مشروع التخرج 1": ["اجتياز 90 ساعة معتمدة"],

    "Graduation Project 2": ["Graduation Project 1"],
    "مشروع التخرج 2": ["مشروع التخرج 1"],

    "Training": ["Passed 90 Credit Hours"],
    "التدريب": ["اجتياز 90 ساعة معتمدة"]
}





CIS_prerequisites = {
    # السنة الأولى
    "Discrete": [],
    "الرياضيات المتقطعة": [],

    "Computer 99": [],
    "مقدمة في الحاسوب": [],

    "C++": ["Computer 99"],
    "سي بلس بلس": ["مقدمة في الحاسوب"],

    "OOP": ["Computer 99", "C++"],
    "البرمجة الكائنية": ["مقدمة في الحاسوب", "سي بلس بلس"],

    "Fundamentals": [],
    "أساسيات الحوسبة": [],

    "Web": ["Computer 99", "C++"],
    "تصميم الويب": ["مقدمة في الحاسوب", "سي بلس بلس"],

    "Statistics": [],
    "الإحصاء": [],

    "Calculus 1": [],
    "التفاضل والتكامل 1": [],

    "Linear CS": ["Calculus 1"],
    "الجبر الخطي في علوم الحاسوب": ["التفاضل والتكامل 1"],

    # السنة الثانية
    "Ethics & Doc": ["Fundamentals"],
    "الأخلاقيات والتوثيق": ["أساسيات الحوسبة"],

    "Adv Java": ["Computer 99", "C++", "OOP"],
    "الجافا المتقدمة": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية"],

    "Database": ["Computer 99", "C++", "OOP"],
    "قواعد البيانات": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية"],

    "Networks": ["Computer 99", "C++", "OOP"],
    "الشبكات": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية"],

    "Data Structures": ["Computer 99", "C++", "OOP"],
    "هياكل البيانات": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية"],

    "Info System": ["Computer 99", "C++", "OOP", "Database"],
    "نظم المعلومات": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "قواعد البيانات"],

    "Algorithm": ["Computer 99", "C++", "OOP", "Data Structures"],
    "الخوارزميات": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "هياكل البيانات"],

    "Graphics": ["Computer 99", "C++", "OOP", "Data Structures"],
    "رسومات الحاسوب": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "هياكل البيانات"],

    # السنة الثالثة
    "Seminar": [],
    "ندوة": [],

    "HCI": ["Computer 99", "C++", "OOP", "Web"],
    "التفاعل بين الإنسان والحاسوب": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "تصميم الويب"],

    "CAL": ["Computer 99", "C++", "OOP", "Web"],
    "التعلم بمساعدة الحاسوب": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "تصميم الويب"],

    "Mobile Dev": ["Computer 99", "C++", "OOP", "Web"],
    "تطوير تطبيقات الهواتف": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "تصميم الويب"],

    "Adv DB": ["Computer 99", "C++", "OOP", "Database"],
    "قواعد البيانات المتقدمة": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "قواعد البيانات"],

    "Info Security": ["Computer 99", "C++", "OOP", "Database"],
    "أمن المعلومات": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "قواعد البيانات"],

    "Software": ["Computer 99", "C++", "OOP", "Database"],
    "هندسة البرمجيات": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "قواعد البيانات"],

    "AI": ["Computer 99", "C++", "OOP", "Data Structures"],
    "الذكاء الاصطناعي": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "هياكل البيانات"],

    "Multimedia": ["Computer 99", "C++", "OOP", "Data Structures"],
    "الوسائط المتعددة": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "هياكل البيانات"],

    # السنة الرابعة
    "OS": ["Computer 99", "C++", "OOP", "Data Structures"],
    "أنظمة التشغيل": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "هياكل البيانات"],

    "Project Management": ["Computer 99", "C++", "OOP", "Database", "Software"],
    "إدارة المشاريع": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "قواعد البيانات", "هندسة البرمجيات"],

    "Adv Software": ["Computer 99", "C++", "OOP", "Database", "Software"],
    "هندسة البرمجيات المتقدمة": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "قواعد البيانات", "هندسة البرمجيات"],

    "System": ["Computer 99", "C++", "OOP", "Database", "Software"],
    "النظم البرمجية": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "قواعد البيانات", "هندسة البرمجيات"],

    "GIS": ["Computer 99", "C++", "OOP", "Data Structures", "Graphics"],
    "نظم المعلومات الجغرافية": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "هياكل البيانات", "رسومات الحاسوب"],

    "Image": ["Computer 99", "C++", "OOP", "Data Structures", "Graphics"],
    "معالجة الصور": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "هياكل البيانات", "رسومات الحاسوب"],

    "Graduation Project 1": ["Passed 90 Credit Hours"],
    "مشروع التخرج 1": ["اجتياز 90 ساعة معتمدة"],

    "Graduation Project 2": ["Graduation Project 1"],
    "مشروع التخرج 2": ["مشروع التخرج 1"],

    "Training": ["Passed 90 Credit Hours"],
    "التدريب": ["اجتياز 90 ساعة معتمدة"]
}




BIT_prerequisites = {
    # السنة الأولى
    "Computer 99": [],
    "مقدمة في الحاسوب": [],

    "Fundamentals": [],
    "أساسيات الحوسبة": [],

    "C++": ["Computer 99"],
    "سي بلس بلس": ["مقدمة في الحاسوب"],

    "Web": ["Computer 99", "C++"],
    "تصميم الويب": ["مقدمة في الحاسوب", "سي بلس بلس"],

    "OOP": ["Computer 99", "C++"],
    "البرمجة الكائنية": ["مقدمة في الحاسوب", "سي بلس بلس"],

    "Calculus 1": [],
    "التفاضل والتكامل 1": [],

    "Linear Algebra": ["Calculus 1"],
    "الجبر الخطي": ["التفاضل والتكامل 1"],

    "Discrete": [],
    "الرياضيات المتقطعة": [],

    # السنة الثانية
    "MIS": ["Fundamentals"],
    "نظم المعلومات الإدارية": ["أساسيات الحوسبة"],

    "Adv Web": ["Computer 99", "C++", "Web"],
    "تصميم الويب المتقدم": ["مقدمة في الحاسوب", "سي بلس بلس", "تصميم الويب"],

    "Database": ["Computer 99", "C++", "OOP"],
    "قواعد البيانات": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية"],

    "Data Structures": ["Computer 99", "C++", "OOP"],
    "هياكل البيانات": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية"],

    "Networks": ["Computer 99", "C++", "OOP"],
    "الشبكات": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية"],

    "Algorithm": ["Computer 99", "C++", "OOP", "Data Structures"],
    "الخوارزميات": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "هياكل البيانات"],

    "Statistical Packages": ["Discrete"],
    "حزم الإحصاء": ["الرياضيات المتقطعة"],

    "BI": ["Discrete", "Statistical Packages"],
    "ذكاء الأعمال": ["الرياضيات المتقطعة", "حزم الإحصاء"],

    # السنة الثالثة
    "Ethics": ["Fundamentals"],
    "أخلاقيات الحوسبة": ["أساسيات الحوسبة"],

    "WSP": ["Computer 99", "C++", "Web"],
    "معالجة خدمات الويب": ["مقدمة في الحاسوب", "سي بلس بلس", "تصميم الويب"],

    "E-business": ["Computer 99", "C++", "Web", "WSP"],
    "الأعمال الإلكترونية": ["مقدمة في الحاسوب", "سي بلس بلس", "تصميم الويب", "معالجة خدمات الويب"],

    "Mobile programming": ["Computer 99", "C++", "Web", "Adv Web"],
    "برمجة تطبيقات الهاتف": ["مقدمة في الحاسوب", "سي بلس بلس", "تصميم الويب", "تصميم الويب المتقدم"],

    "Info Security": ["Computer 99", "C++", "OOP", "Database"],
    "أمن المعلومات": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "قواعد البيانات"],

    "Software": ["Computer 99", "C++", "OOP", "Database"],
    "هندسة البرمجيات": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "قواعد البيانات"],

    "KMS": ["Discrete"],
    "نظم إدارة المعرفة": ["الرياضيات المتقطعة"],

    "System": ["Computer 99", "C++", "OOP", "Database", "Software"],
    "نظم المعلومات": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "قواعد البيانات", "هندسة البرمجيات"],

    "ERP": ["Computer 99", "C++", "OOP", "Data Structures", "Algorithms"],
    "نظم تخطيط موارد المؤسسات": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "هياكل البيانات", "الخوارزميات"],

    "Seminar": [],
    "ندوة": [],

    # السنة الرابعة
    "TQM": ["Computer 99", "C++", "OOP", "Database", "Software"],
    "إدارة الجودة الشاملة": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "قواعد البيانات", "هندسة البرمجيات"],

    "OS": ["Computer 99", "C++", "OOP", "Data Structures"],
    "أنظمة التشغيل": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "هياكل البيانات"],

    "Simulation": ["Computer 99", "C++", "OOP", "Data Structures"],
    "المحاكاة": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "هياكل البيانات"],

    "E-payment": ["Computer 99", "C++", "OOP", "Database", "Info Security"],
    "أنظمة الدفع الإلكتروني": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "قواعد البيانات", "أمن المعلومات"],

    "Project Management": ["Computer 99", "C++", "OOP", "Database", "Software"],
    "إدارة المشاريع": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "قواعد البيانات", "هندسة البرمجيات"],

    "Document Analysis": ["Computer 99", "C++", "OOP", "Data Structures", "Algorithms"],
    "تحليل الوثائق": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "هياكل البيانات", "الخوارزميات"],

    "Graduation Project 1": ["Passed 90 Credit Hours"],
    "مشروع التخرج 1": ["اجتياز 90 ساعة معتمدة"],

    "Graduation Project 2": ["Graduation Project 1"],
    "مشروع التخرج 2": ["مشروع التخرج 1"],

    "Training": ["Passed 90 Credit Hours"],
    "التدريب": ["اجتياز 90 ساعة معتمدة"]
}




Cyber_prerequisites = {
    # السنة الأولى
    "Computer 99": [],
    "مقدمة في الحاسوب": [],

    "Fundamentals": [],
    "أساسيات الحوسبة": [],

    "C++": ["Computer 99"],
    "سي بلس بلس": ["مقدمة في الحاسوب"],

    "Web": ["Computer 99", "C++"],
    "تصميم الويب": ["مقدمة في الحاسوب", "سي بلس بلس"],

    "OOP": ["Computer 99", "C++"],
    "البرمجة الكائنية": ["مقدمة في الحاسوب", "سي بلس بلس"],

    "Calculus 1": [],
    "التفاضل والتكامل 1": [],

    "Linear Algebra": ["Calculus 1"],
    "الجبر الخطي": ["التفاضل والتكامل 1"],

    "Discrete": [],
    "الرياضيات المتقطعة": [],

    "Principles of Security": [],
    "مبادئ الأمن السيبراني": [],

    # السنة الثانية
    "Data Structures": ["Computer 99", "C++", "OOP"],
    "هياكل البيانات": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية"],

    "Programming for Cyber Security": ["Computer 99", "C++", "OOP"],
    "برمجة الأمن السيبراني": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية"],

    "Database": ["Computer 99", "C++", "OOP"],
    "قواعد البيانات": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية"],

    "Cryptography": ["Principles of Security"],
    "التشفير": ["مبادئ الأمن السيبراني"],

    "Security & Ethics": ["Principles of Security"],
    "الأمن والأخلاقيات": ["مبادئ الأمن السيبراني"],

    "Statistics": [],
    "الإحصاء": [],

    "Computer Architecture": ["Fundamentals or Discrete"],
    "بنية الحاسوب": ["أساسيات الحوسبة أو الرياضيات المتقطعة"],

    # السنة الثالثة
    "Web Security": ["Computer 99", "C++", "Web"],
    "أمن الويب": ["مقدمة في الحاسوب", "سي بلس بلس", "تصميم الويب"],

    "Seminars": [],
    "ندوة": [],

    "Networks": ["Computer 99", "C++", "OOP"],
    "الشبكات": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية"],

    "Hacking": ["Computer 99", "C++", "OOP", "Networks"],
    "الاختراق الأخلاقي": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "الشبكات"],

    "Network Security": ["Computer 99", "C++", "OOP", "Networks"],
    "أمن الشبكات": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "الشبكات"],

    "AI": ["Computer 99", "C++", "OOP", "Data Structures"],
    "الذكاء الاصطناعي": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "هياكل البيانات"],

    "Algorithms": ["Computer 99", "C++", "OOP", "Data Structures"],
    "الخوارزميات": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "هياكل البيانات"],

    "Software": ["Computer 99", "C++", "OOP", "Database"],
    "هندسة البرمجيات": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "قواعد البيانات"],

    # السنة الرابعة
    "Authentication": ["Computer 99", "C++", "OOP", "Networks"],
    "المصادقة": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "الشبكات"],

    "Digital Forensics": ["Computer 99", "C++", "OOP", "Networks"],
    "الطب الشرعي الرقمي": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "الشبكات"],

    "OS": ["Computer 99", "C++", "OOP", "Data Structures"],
    "أنظمة التشغيل": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "هياكل البيانات"],

    "CPSS": ["Computer 99", "C++", "OOP", "Networks", "Network Security"],
    "أمن الأنظمة الإلكترونية": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "الشبكات", "أمن الشبكات"],

    "SI": ["Computer 99", "C++", "OOP", "Data Structures", "AI"],
    "أنظمة الذكاء": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "هياكل البيانات", "الذكاء الاصطناعي"],

    "Reverse Engineering": ["Computer 99", "C++", "OOP", "Database", "Software"],
    "الهندسة العكسية": ["مقدمة في الحاسوب", "سي بلس بلس", "البرمجة الكائنية", "قواعد البيانات", "هندسة البرمجيات"],

    "Graduation Project 1": ["Passed 90 Credit Hours"],
    "مشروع التخرج 1": ["اجتياز 90 ساعة معتمدة"],

    "Graduation Project 2": ["Graduation Project 1"],
    "مشروع التخرج 2": ["مشروع التخرج 1"],

    "Training": ["Passed 90 Credit Hours"],
    "التدريب": ["اجتياز 90 ساعة معتمدة"]
}




course_descriptions = {
    "Calculus 1": {
        "arabic_name": "التفاضل والتكامل 1",
        "description_en": "An introduction to limits, derivatives, and integrals, focusing on differentiation and its applications in science and engineering.",
        "description_ar": "مقدمة في النهايات والمشتقات والتكاملات، مع التركيز على التفاضل وتطبيقاته في العلوم والهندسة."
    },
    "Discrete Mathematics": {
        "arabic_name": "الرياضيات المتقطعة",
        "description_en": "Covers logic, set theory, combinatorics, graph theory, and algorithms essential for computing.",
        "description_ar": "يغطي المنطق، نظرية المجموعات، التوافيق، نظرية الرسوم البيانية، والخوارزميات الضرورية للحوسبة."
    },
    "Statistics": {
        "arabic_name": "الإحصاء",
        "description_en": "Introduces probability, descriptive and inferential statistics, hypothesis testing, and regression analysis.",
        "description_ar": "مقدمة في الاحتمالات، الإحصاء الوصفي والاستنتاجي، اختبار الفرضيات، وتحليل الانحدار."
    },
    "Computer 99": {
        "arabic_name": "مقدمة في الحاسوب",
        "description_en": "Basic introduction to computer systems, software applications, and problem-solving using programming.",
        "description_ar": "مقدمة في أنظمة الحاسوب، التطبيقات البرمجية، وحل المشكلات باستخدام البرمجة."
    },
    "Principles of Data Science": {
        "arabic_name": "مبادئ علم البيانات",
        "description_en": "Covers data collection, cleaning, visualization, statistical analysis, and introductory machine learning concepts.",
        "description_ar": "يغطي جمع البيانات، تنظيفها، تصورها، التحليل الإحصائي، ومفاهيم تعلم الآلة الأساسية."
    },
    "Fundamentals": {
        "arabic_name": "أساسيات الحوسبة",
        "description_en": "Introduction to computing principles, data representation, algorithms, and basic programming logic.",
        "description_ar": "مقدمة في مبادئ الحوسبة، تمثيل البيانات، الخوارزميات، والمنطق البرمجي الأساسي."
    },
    "C++": {
        "arabic_name": "سي بلس بلس",
        "description_en": "Covers C++ syntax, control structures, functions, and object-oriented programming concepts.",
        "description_ar": "يغطي بناء الجمل البرمجية في C++، الهياكل التحكمية، الدوال، ومفاهيم البرمجة الكائنية."
    },
    "Linear Algebra": {
        "arabic_name": "الجبر الخطي",
        "description_en": "Explores vector spaces, matrices, determinants, eigenvalues, and linear transformations.",
        "description_ar": "يدرس الفضاءات المتجهية، المصفوفات، المحددات، القيم الذاتية، والتحويلات الخطية."
    },
    "OOP": {
        "arabic_name": "البرمجة الكائنية",
        "description_en": "Focuses on object-oriented concepts such as classes, inheritance, polymorphism, and encapsulation.",
        "description_ar": "يركز على مفاهيم البرمجة الكائنية مثل الفئات، الوراثة، تعدد الأشكال، والتغليف."
    },
    "Data Engineering": {
        "arabic_name": "هندسة البيانات",
        "description_en": "Introduction to data pipelines, ETL processes, database management, and big data handling.",
        "description_ar": "مقدمة في خطوط البيانات، عمليات الاستخراج والتحويل والتحميل (ETL)، وإدارة قواعد البيانات والتعامل مع البيانات الضخمة."
    },
    "Applied Statistics": {
        "arabic_name": "الإحصاء التطبيقي",
        "description_en": "Application of statistical methods in data analysis, regression models, and hypothesis testing.",
        "description_ar": "تطبيق الأساليب الإحصائية في تحليل البيانات، نماذج الانحدار، واختبار الفرضيات."
    },
    "AI Programming": {
        "arabic_name": "برمجة الذكاء الاصطناعي",
        "description_en": "Covers Python programming for AI, machine learning frameworks, and algorithm development.",
        "description_ar": "يغطي برمجة بايثون للذكاء الاصطناعي، أطر تعلم الآلة، وتطوير الخوارزميات."
    },
    "Database": {
        "arabic_name": "قواعد البيانات",
        "description_en": "Introduction to relational databases, SQL queries, normalization, and database design principles.",
        "description_ar": "مقدمة في قواعد البيانات العلائقية، استعلامات SQL، التطبيع، ومبادئ تصميم قواعد البيانات."
    },
    "Data Structures": {
        "arabic_name": "هياكل البيانات",
        "description_en": "Explores fundamental data structures such as arrays, linked lists, stacks, queues, trees, and graphs.",
        "description_ar": "يدرس هياكل البيانات الأساسية مثل المصفوفات، القوائم المتصلة، المكدسات، الطوابير، الأشجار، والرسوم البيانية."
    },
    "Data Mining": {
        "arabic_name": "تنقيب البيانات",
        "description_en": "Focuses on techniques for discovering patterns in large datasets, including clustering, classification, and association rules.",
        "description_ar": "يركز على تقنيات اكتشاف الأنماط في مجموعات البيانات الكبيرة، بما في ذلك التجميع، التصنيف، وقواعد الارتباط."
    },
        "Algorithms": {
        "arabic_name": "الخوارزميات",
        "description_en": "Explores fundamental algorithm design techniques, including divide and conquer, dynamic programming, and graph algorithms.",
        "description_ar": "يستكشف تقنيات تصميم الخوارزميات الأساسية، بما في ذلك التقسيم والتغلب، البرمجة الديناميكية، وخوارزميات الرسوم البيانية."
    },
    "Ethics AI & DS": {
        "arabic_name": "أخلاقيات الذكاء الاصطناعي وعلم البيانات",
        "description_en": "Discusses ethical concerns in AI and data science, including bias, privacy, and responsible AI development.",
        "description_ar": "يناقش القضايا الأخلاقية في الذكاء الاصطناعي وعلم البيانات، بما في ذلك التحيز، الخصوصية، وتطوير الذكاء الاصطناعي المسؤول."
    },
    "Seminar": {
        "arabic_name": "ندوة",
        "description_en": "A research-based seminar where students present and discuss emerging topics in their field.",
        "description_ar": "ندوة بحثية يقدّم فيها الطلاب مواضيع ناشئة في مجالهم ويتم مناقشتها."
    },
    "Networks": {
        "arabic_name": "الشبكات",
        "description_en": "Covers network architectures, protocols, data communication principles, and security measures.",
        "description_ar": "يغطي بنى الشبكات، البروتوكولات، مبادئ الاتصال بين البيانات، وإجراءات الأمان."
    },
    "Information Security": {
        "arabic_name": "أمن المعلومات",
        "description_en": "Introduces cryptographic techniques, risk management, network security, and cybersecurity policies.",
        "description_ar": "مقدمة في تقنيات التشفير، إدارة المخاطر، أمن الشبكات، وسياسات الأمن السيبراني."
    },
    "Unstructured Database": {
        "arabic_name": "قواعد البيانات غير المنظمة",
        "description_en": "Focuses on NoSQL databases, document stores, key-value stores, and handling large-scale unstructured data.",
        "description_ar": "يركز على قواعد البيانات غير العلائقية (NoSQL)، تخزين الوثائق، تخزين القيم الرئيسية، والتعامل مع البيانات غير المنظمة على نطاق واسع."
    },
    "Software": {
        "arabic_name": "هندسة البرمجيات",
        "description_en": "Covers software development methodologies, software lifecycle, design patterns, and project management techniques.",
        "description_ar": "يغطي منهجيات تطوير البرمجيات، دورة حياة البرمجيات، أنماط التصميم، وتقنيات إدارة المشاريع."
    },
    "Pattern & Analysis": {
        "arabic_name": "تحليل الأنماط",
        "description_en": "Explores pattern recognition techniques, including feature extraction, classification, and clustering.",
        "description_ar": "يستكشف تقنيات التعرف على الأنماط، بما في ذلك استخراج الميزات، التصنيف، والتجميع."
    },
    "Machine Learning": {
        "arabic_name": "تعلم الآلة",
        "description_en": "Introduces supervised and unsupervised learning models, neural networks, and deep learning techniques.",
        "description_ar": "مقدمة في نماذج التعلم الموجّه وغير الموجّه، الشبكات العصبية، وتقنيات التعلم العميق."
    },
    "AI": {
        "arabic_name": "الذكاء الاصطناعي",
        "description_en": "Covers AI techniques, problem-solving strategies, heuristic search, expert systems, and neural networks.",
        "description_ar": "يغطي تقنيات الذكاء الاصطناعي، استراتيجيات حل المشكلات، البحث التجريبي، الأنظمة الخبيرة، والشبكات العصبية."
    },
    "Cloud Computing": {
        "arabic_name": "الحوسبة السحابية",
        "description_en": "Explores cloud services, virtualization, distributed computing, and cloud security concepts.",
        "description_ar": "يستكشف خدمات الحوسبة السحابية، الافتراضية، الحوسبة الموزعة، ومفاهيم أمان السحابة."
    },
    "Big Data": {
        "arabic_name": "البيانات الضخمة",
        "description_en": "Focuses on big data processing, storage solutions, Hadoop ecosystem, and real-time analytics.",
        "description_ar": "يركز على معالجة البيانات الضخمة، حلول التخزين، بيئة Hadoop، والتحليلات في الوقت الفعلي."
    },
    "Deep Learning": {
        "arabic_name": "التعلم العميق",
        "description_en": "Advanced course covering deep neural networks, CNNs, RNNs, GANs, and their applications.",
        "description_ar": "دورة متقدمة تغطي الشبكات العصبية العميقة، الشبكات العصبية التلافيفية، الشبكات العصبية المتكررة، والشبكات التوليدية."
    },
    "Form Publishing": {
        "arabic_name": "نشر النماذج",
        "description_en": "Covers model deployment strategies, API integrations, and scalable AI applications.",
        "description_ar": "يغطي استراتيجيات نشر النماذج، تكاملات API، وتطبيقات الذكاء الاصطناعي القابلة للتطوير."
    },
    "Data Visualization": {
        "arabic_name": "تصور البيانات",
        "description_en": "Explores techniques for visualizing structured and unstructured data using charts, graphs, and dashboards.",
        "description_ar": "يستكشف تقنيات تصور البيانات المنظمة وغير المنظمة باستخدام الرسوم البيانية والمخططات ولوحات المعلومات."
    },
    "NLP": {
        "arabic_name": "معالجة اللغة الطبيعية",
        "description_en": "Introduces text processing, sentiment analysis, tokenization, and machine translation.",
        "description_ar": "مقدمة في معالجة النصوص، تحليل المشاعر، تجزئة النصوص، والترجمة الآلية."
    },
    "Graduation Project 1": {
        "arabic_name": "مشروع التخرج 1",
        "description_en": "A capstone project where students apply theoretical knowledge to develop a real-world application.",
        "description_ar": "مشروع تخرج يقوم فيه الطلاب بتطبيق المعرفة النظرية لتطوير تطبيق عملي."
    },
    "Graduation Project 2": {
        "arabic_name": "مشروع التخرج 2",
        "description_en": "Continuation of Graduation Project 1, focusing on project implementation and finalization.",
        "description_ar": "استكمال لمشروع التخرج 1، يركز على تنفيذ المشروع وإنجازه النهائي."
    },
    "Training": {
        "arabic_name": "التدريب",
        "description_en": "An internship where students gain practical experience in industry settings.",
        "description_ar": "تدريب عملي يكتسب فيه الطلاب خبرة عملية في بيئات صناعية."
    },
        "Intro to AI": {
        "arabic_name": "مقدمة في الذكاء الاصطناعي",
        "description_en": "An introduction to artificial intelligence concepts, including intelligent agents, problem-solving techniques, and search algorithms.",
        "description_ar": "مقدمة في مفاهيم الذكاء الاصطناعي، بما في ذلك الوكلاء الأذكياء، تقنيات حل المشكلات، وخوارزميات البحث."
    },
    "Knowledge & Reasoning": {
        "arabic_name": "تمثيل واستخراج المعرفة",
        "description_en": "Covers logical representation of knowledge, reasoning techniques, and inference mechanisms in AI.",
        "description_ar": "يغطي تمثيل المعرفة بشكل منطقي، تقنيات الاستدلال، وآليات الاستنتاج في الذكاء الاصطناعي."
    },
    "HCI": {
        "arabic_name": "التفاعل بين الإنسان والحاسوب",
        "description_en": "Focuses on designing and evaluating user-friendly human-computer interactions using UX/UI principles.",
        "description_ar": "يركز على تصميم وتقييم التفاعل بين الإنسان والحاسوب باستخدام مبادئ تجربة المستخدم وواجهة المستخدم."
    },
    "Embedded System": {
        "arabic_name": "الأنظمة المدمجة",
        "description_en": "Explores hardware-software integration, real-time operating systems, and microcontroller programming.",
        "description_ar": "يستكشف تكامل الأجهزة والبرمجيات، أنظمة التشغيل في الزمن الحقيقي، وبرمجة المتحكمات الدقيقة."
    },
    "Ontologies": {
        "arabic_name": "الأنطولوجيا والتمثيل المعرفي",
        "description_en": "Introduces semantic web technologies, ontology engineering, and knowledge-based AI systems.",
        "description_ar": "يقدم تقنيات الويب الدلالي، هندسة الأنطولوجيا، والأنظمة الذكية القائمة على المعرفة."
    },
    "Computer Vision": {
        "arabic_name": "الرؤية الحاسوبية",
        "description_en": "Covers image processing, object detection, pattern recognition, and deep learning applications in vision.",
        "description_ar": "يغطي معالجة الصور، كشف الأجسام، التعرف على الأنماط، وتطبيقات التعلم العميق في الرؤية الحاسوبية."
    },
    "Robotics": {
        "arabic_name": "الروبوتات الذكية",
        "description_en": "Explores autonomous robots, sensor integration, motion planning, and reinforcement learning techniques.",
        "description_ar": "يستكشف الروبوتات المستقلة، تكامل المستشعرات، تخطيط الحركة، وتقنيات التعلم المعزز."
    },
    "Cognitive": {
        "arabic_name": "علوم الإدراك",
        "description_en": "Focuses on cognitive computing, human-like reasoning models, and AI-driven decision-making systems.",
        "description_ar": "يركز على الحوسبة الإدراكية، نماذج التفكير المشابهة للبشر، وأنظمة اتخاذ القرار المعتمدة على الذكاء الاصطناعي."
    },
    "IOT": {
        "arabic_name": "إنترنت الأشياء",
        "description_en": "Explores IoT architectures, embedded systems, cloud integration, and smart devices.",
        "description_ar": "يستكشف بنى إنترنت الأشياء، الأنظمة المدمجة، تكامل السحابة، والأجهزة الذكية."
    },
    "Physics": {
        "arabic_name": "الفيزياء",
        "description_en": "Fundamentals of classical and modern physics, covering mechanics, thermodynamics, and electromagnetism.",
        "description_ar": "أساسيات الفيزياء الكلاسيكية والحديثة، تغطي الميكانيكا، الديناميكا الحرارية، والكهرومغناطيسية."
    },
    "Linear CS": {
        "arabic_name": "الجبر الخطي لعلوم الحاسوب",
        "description_en": "Covers matrix operations, vector spaces, and applications of linear algebra in computing.",
        "description_ar": "يغطي عمليات المصفوفات، الفضاءات المتجهية، وتطبيقات الجبر الخطي في علوم الحاسوب."
    },
    "Calculus 2": {
        "arabic_name": "التفاضل والتكامل 2",
        "description_en": "Extends concepts from Calculus 1, including integration techniques, sequences, and series.",
        "description_ar": "يمتد إلى مفاهيم التفاضل والتكامل 1، بما في ذلك تقنيات التكامل، المتتاليات، والمتسلسلات."
    },
    "Numerical": {
        "arabic_name": "التحليل العددي",
        "description_en": "Explores numerical methods for solving mathematical problems in computing, including interpolation and approximation.",
        "description_ar": "يستكشف الطرق العددية لحل المشكلات الرياضية في الحوسبة، بما في ذلك الاستيفاء والتقريب."
    },
    "Theory": {
        "arabic_name": "نظرية الحوسبة",
        "description_en": "Introduces automata theory, formal languages, and computability concepts.",
        "description_ar": "يقدم نظرية الآلات، اللغات الشكلية، ومفاهيم الحسابية."
    },
    "Logic": {
        "arabic_name": "المنطق الرياضي",
        "description_en": "Covers propositional logic, predicate logic, and applications in AI and computer science.",
        "description_ar": "يغطي المنطق الاقتراحي، المنطق الحملي، وتطبيقاته في الذكاء الاصطناعي وعلوم الحاسوب."
    },
    "Advanced Programming": {
        "arabic_name": "البرمجة المتقدمة",
        "description_en": "Covers advanced programming paradigms, software architecture, and efficient coding techniques.",
        "description_ar": "يغطي أنماط البرمجة المتقدمة، هندسة البرمجيات، وتقنيات البرمجة الفعالة."
    },
    "Organization": {
        "arabic_name": "تنظيم الحاسوب",
        "description_en": "Examines the design and functionality of computer architecture, memory management, and instruction execution.",
        "description_ar": "يدرس تصميم وعمل معمارية الحاسوب، إدارة الذاكرة، وتنفيذ التعليمات."
    },
    "Simulation": {
        "arabic_name": "المحاكاة",
        "description_en": "Covers modeling and simulation techniques used in computing and engineering applications.",
        "description_ar": "يغطي تقنيات النمذجة والمحاكاة المستخدمة في التطبيقات الحاسوبية والهندسية."
    },
    "Graphics": {
        "arabic_name": "الرسوميات الحاسوبية",
        "description_en": "Explores 2D and 3D rendering, OpenGL programming, and visualization techniques.",
        "description_ar": "يستكشف التصيير ثنائي وثلاثي الأبعاد، برمجة OpenGL، وتقنيات التصور."
    },
    "Ethics": {
        "arabic_name": "أخلاقيات الحوسبة",
        "description_en": "Discusses ethical dilemmas in computing, including privacy, cybersecurity, and AI ethics.",
        "description_ar": "يناقش القضايا الأخلاقية في الحوسبة، بما في ذلك الخصوصية، الأمن السيبراني، وأخلاقيات الذكاء الاصطناعي."
    },
    "PL": {
        "arabic_name": "لغات البرمجة",
        "description_en": "Introduces programming language concepts, including syntax, semantics, and language paradigms.",
        "description_ar": "يقدم مفاهيم لغات البرمجة، بما في ذلك البنية النحوية، الدلالات، وأنماط البرمجة."
    },
    "Compiler": {
        "arabic_name": "المترجمات",
        "description_en": "Explores lexical analysis, parsing, syntax-directed translation, and compiler construction.",
        "description_ar": "يستكشف تحليل الكلمات، التحليل النحوي، الترجمة الموجهة بالنحو، وبناء المترجمات."
    },
    "Security": {
        "arabic_name": "أمن المعلومات",
        "description_en": "Focuses on network security, cryptography, ethical hacking, and cybersecurity policies.",
        "description_ar": "يركز على أمن الشبكات، التشفير، الاختراق الأخلاقي، وسياسات الأمن السيبراني."
    },
    "Parallel": {
        "arabic_name": "الحوسبة المتوازية",
        "description_en": "Covers parallel processing techniques, GPU programming, and distributed computing models.",
        "description_ar": "يغطي تقنيات المعالجة المتوازية، برمجة وحدات المعالجة الرسومية، ونماذج الحوسبة الموزعة."
    },
    "Computational Problem": {
        "arabic_name": "المشاكل الحاسوبية",
        "description_en": "Examines problem-solving strategies in computing, complexity theory, and P vs NP problems.",
        "description_ar": "يدرس استراتيجيات حل المشكلات في الحوسبة، نظرية التعقيد، ومشاكل P مقابل NP."
    },
    "OS": {
        "arabic_name": "أنظمة التشغيل",
        "description_en": "Covers operating system fundamentals, process management, memory allocation, and file systems.",
        "description_ar": "يغطي أساسيات أنظمة التشغيل، إدارة العمليات، تخصيص الذاكرة، وأنظمة الملفات."
    },
        "MIS": {
        "arabic_name": "نظم المعلومات الإدارية",
        "description_en": "Covers fundamental concepts of Management Information Systems (MIS), including how technology supports decision-making, business processes, and organizational strategy.",
        "description_ar": "يغطي المفاهيم الأساسية لنظم المعلومات الإدارية (MIS)، بما في ذلك كيفية دعم التكنولوجيا لاتخاذ القرار والعمليات التجارية واستراتيجية المؤسسات."
    },
    "Adv Web": {
        "arabic_name": "تصميم الويب المتقدم",
        "description_en": "Explores advanced web development techniques, including server-side scripting, front-end frameworks, database connectivity, and API integration.",
        "description_ar": "يستكشف تقنيات تطوير الويب المتقدمة، بما في ذلك البرمجة من جهة الخادم، أطر العمل الخاصة بالواجهة الأمامية، الاتصال بقاعدة البيانات، وتكامل واجهات البرمجة."
    },
    "Statistical Packages": {
        "arabic_name": "حزم الإحصاء",
        "description_en": "Focuses on statistical analysis using software like SPSS, R, and Python, covering data visualization, hypothesis testing, and predictive modeling.",
        "description_ar": "يركز على التحليل الإحصائي باستخدام برامج مثل SPSS و R و Python، مع تغطية تصوّر البيانات، واختبار الفرضيات، والنمذجة التنبؤية."
    },
    "BI": {
        "arabic_name": "ذكاء الأعمال",
        "description_en": "Introduces Business Intelligence (BI) tools and techniques for data-driven decision-making, including dashboards, data warehousing, and reporting.",
        "description_ar": "يقدم أدوات وتقنيات ذكاء الأعمال (BI) لاتخاذ القرارات بناءً على البيانات، بما في ذلك لوحات المعلومات، ومستودعات البيانات، والتقارير."
    },
    "WSP": {
        "arabic_name": "معالجة خدمات الويب",
        "description_en": "Focuses on Web Services Processing (WSP), including RESTful and SOAP-based services, API development, and microservices architecture.",
        "description_ar": "يركز على معالجة خدمات الويب (WSP)، بما في ذلك الخدمات القائمة على RESTful و SOAP، وتطوير واجهات برمجة التطبيقات (APIs)، وهندسة الخدمات المصغرة."
    },
    "E-business": {
        "arabic_name": "الأعمال الإلكترونية",
        "description_en": "Covers electronic commerce principles, online payment systems, digital marketing strategies, and e-business models.",
        "description_ar": "يغطي مبادئ التجارة الإلكترونية، أنظمة الدفع عبر الإنترنت، استراتيجيات التسويق الرقمي، ونماذج الأعمال الإلكترونية."
    },
    "Mobile programming": {
        "arabic_name": "برمجة تطبيقات الهاتف",
        "description_en": "Explores mobile app development for Android and iOS, including UI/UX design, database integration, and app deployment.",
        "description_ar": "يستكشف تطوير تطبيقات الهواتف المحمولة لنظامي Android و iOS، بما في ذلك تصميم واجهة المستخدم وتجربة المستخدم، وتكامل قواعد البيانات، ونشر التطبيقات."
    },
    "KMS": {
        "arabic_name": "نظم إدارة المعرفة",
        "description_en": "Discusses Knowledge Management Systems (KMS) and their role in capturing, sharing, and utilizing organizational knowledge.",
        "description_ar": "يناقش نظم إدارة المعرفة (KMS) ودورها في التقاط المعرفة المؤسسية ومشاركتها والاستفادة منها."
    },
    "System": {
        "arabic_name": "نظم المعلومات",
        "description_en": "Introduces Information Systems (IS) concepts, including system development life cycle, enterprise systems, and decision support systems.",
        "description_ar": "يقدم مفاهيم نظم المعلومات (IS)، بما في ذلك دورة حياة تطوير النظم، الأنظمة المؤسسية، ونظم دعم القرار."
    },
    "ERP": {
        "arabic_name": "نظم تخطيط موارد المؤسسات",
        "description_en": "Covers Enterprise Resource Planning (ERP) systems, their implementation, and integration with business processes.",
        "description_ar": "يغطي أنظمة تخطيط موارد المؤسسات (ERP)، تنفيذها، وتكاملها مع العمليات التجارية."
    },
    "TQM": {
        "arabic_name": "إدارة الجودة الشاملة",
        "description_en": "Focuses on Total Quality Management (TQM) methodologies, including Six Sigma, ISO standards, and continuous improvement techniques.",
        "description_ar": "يركز على منهجيات إدارة الجودة الشاملة (TQM)، بما في ذلك سيجما 6، معايير ISO، وتقنيات التحسين المستمر."
    },
    "E-payment": {
        "arabic_name": "أنظمة الدفع الإلكتروني",
        "description_en": "Explores electronic payment systems, digital wallets, blockchain-based transactions, and financial security protocols.",
        "description_ar": "يستكشف أنظمة الدفع الإلكتروني، المحافظ الرقمية، المعاملات القائمة على البلوكشين، وبروتوكولات الأمان المالي."
    },
    "Project Management": {
        "arabic_name": "إدارة المشاريع",
        "description_en": "Covers project management principles, agile methodologies, risk management, and project life cycle.",
        "description_ar": "يغطي مبادئ إدارة المشاريع، المنهجيات الرشيقة (Agile)، إدارة المخاطر، ودورة حياة المشروع."
    },
    "Document Analysis": {
        "arabic_name": "تحليل الوثائق",
        "description_en": "Focuses on document processing techniques, text mining, and AI-driven document classification.",
        "description_ar": "يركز على تقنيات معالجة الوثائق، تنقيب النصوص، وتصنيف الوثائق باستخدام الذكاء الاصطناعي."
    },
    "Principles of Security": {
        "arabic_name": "مبادئ الأمن السيبراني",
        "description_en": "Introduces fundamental cybersecurity principles, including threat analysis, cryptographic techniques, and network defense strategies.",
        "description_ar": "يقدم مبادئ الأمن السيبراني الأساسية، بما في ذلك تحليل التهديدات، تقنيات التشفير، واستراتيجيات الدفاع عن الشبكات."
    },
    "Programming for Cyber Security": {
        "arabic_name": "برمجة الأمن السيبراني",
        "description_en": "Covers secure coding practices, vulnerability analysis, and penetration testing for cybersecurity professionals.",
        "description_ar": "يغطي ممارسات البرمجة الآمنة، تحليل الثغرات الأمنية، واختبار الاختراق لمحترفي الأمن السيبراني."
    },
    "Cryptography": {
        "arabic_name": "التشفير",
        "description_en": "Explores encryption techniques, cryptographic algorithms, digital signatures, and secure communication protocols.",
        "description_ar": "يستكشف تقنيات التشفير، الخوارزميات التشفيرية، التوقيعات الرقمية، وبروتوكولات الاتصال الآمنة."
    },
    "Security & Ethics": {
        "arabic_name": "الأمن والأخلاقيات",
        "description_en": "Discusses ethical considerations in cybersecurity, data privacy laws, and responsible AI practices.",
        "description_ar": "يناقش الاعتبارات الأخلاقية في الأمن السيبراني، قوانين خصوصية البيانات، وممارسات الذكاء الاصطناعي المسؤولة."
    },
        "Computer Architecture": {
        "arabic_name": "بنية الحاسوب",
        "description_en": "Covers the fundamental principles of computer organization and architecture, including CPU design, memory hierarchy, instruction sets, and parallel processing.",
        "description_ar": "يغطي المبادئ الأساسية لتنظيم وبنية الحاسوب، بما في ذلك تصميم وحدة المعالجة المركزية، التسلسل الهرمي للذاكرة، مجموعات التعليمات، والمعالجة المتوازية."
    },
    "Web Security": {
        "arabic_name": "أمن الويب",
        "description_en": "Focuses on securing web applications, covering topics such as authentication mechanisms, encryption, session management, and common vulnerabilities like SQL injection and cross-site scripting (XSS).",
        "description_ar": "يركز على تأمين تطبيقات الويب، ويشمل موضوعات مثل آليات المصادقة، التشفير، إدارة الجلسات، والثغرات الشائعة مثل حقن SQL وهجمات البرمجة عبر المواقع (XSS)."
    },
    "Hacking": {
        "arabic_name": "الاختراق الأخلاقي",
        "description_en": "Explores ethical hacking techniques, penetration testing methodologies, and cybersecurity defense mechanisms to assess and improve system security.",
        "description_ar": "يستكشف تقنيات الاختراق الأخلاقي، منهجيات اختبار الاختراق، وآليات الدفاع السيبراني لتقييم وتحسين أمان الأنظمة."
    },
    "Network Security": {
        "arabic_name": "أمن الشبكات",
        "description_en": "Covers network security principles, including firewalls, intrusion detection systems, VPNs, and protocols to safeguard network communications.",
        "description_ar": "يغطي مبادئ أمن الشبكات، بما في ذلك الجدران النارية، أنظمة كشف التسلل، الشبكات الافتراضية الخاصة (VPNs)، والبروتوكولات لحماية الاتصالات الشبكية."
    },
    "Authentication": {
        "arabic_name": "المصادقة",
        "description_en": "Examines authentication mechanisms, multi-factor authentication (MFA), biometrics, and identity management systems for secure access control.",
        "description_ar": "يدرس آليات المصادقة، المصادقة متعددة العوامل (MFA)، القياسات الحيوية، وأنظمة إدارة الهوية للتحكم الآمن في الوصول."
    },
    "Digital Forensics": {
        "arabic_name": "الطب الشرعي الرقمي",
        "description_en": "Introduces digital forensics techniques for investigating cybercrimes, analyzing digital evidence, and recovering data from compromised systems.",
        "description_ar": "يقدم تقنيات الطب الشرعي الرقمي للتحقيق في الجرائم الإلكترونية، وتحليل الأدلة الرقمية، واستعادة البيانات من الأنظمة المخترقة."
    },
    "CPSS": {
        "arabic_name": "أمن الأنظمة الإلكترونية",
        "description_en": "Focuses on the security of cyber-physical systems (CPS), industrial control systems (ICS), and Internet of Things (IoT) security.",
        "description_ar": "يركز على أمان الأنظمة الإلكترونية والفيزيائية (CPS)، وأنظمة التحكم الصناعية (ICS)، وأمن إنترنت الأشياء (IoT)."
    },
    "SI": {
        "arabic_name": "أنظمة الذكاء",
        "description_en": "Explores intelligent systems, including decision support systems, expert systems, and AI-driven automation for real-world applications.",
        "description_ar": "يستكشف أنظمة الذكاء، بما في ذلك أنظمة دعم القرار، والأنظمة الخبيرة، وأتمتة الذكاء الاصطناعي للتطبيقات العملية."
    },
    "Reverse Engineering": {
        "arabic_name": "الهندسة العكسية",
        "description_en": "Introduces reverse engineering techniques for software and hardware, covering binary analysis, malware analysis, and software decompilation.",
        "description_ar": "يقدم تقنيات الهندسة العكسية للبرمجيات والأجهزة، ويشمل تحليل الملفات الثنائية، وتحليل البرمجيات الخبيثة، وإعادة تجميع البرامج."
    },
    "Adv Java": {
        "arabic_name": "الجافا المتقدمة",
        "description_en": "Covers advanced Java programming concepts, including multi-threading, network programming, database connectivity, and GUI development.",
        "description_ar": "يغطي مفاهيم برمجة جافا المتقدمة، بما في ذلك المعالجة المتعددة الخيوط، برمجة الشبكات، الاتصال بقاعدة البيانات، وتطوير واجهات المستخدم الرسومية."
    },
    "Info System": {
        "arabic_name": "نظم المعلومات",
        "description_en": "Explores information system components, design methodologies, and enterprise-level data management strategies.",
        "description_ar": "يستكشف مكونات نظم المعلومات، ومنهجيات التصميم، واستراتيجيات إدارة البيانات على مستوى المؤسسات."
    },
    "CAL": {
        "arabic_name": "التعلم بمساعدة الحاسوب",
        "description_en": "Focuses on Computer-Assisted Learning (CAL) techniques, including e-learning platforms, AI-driven tutoring, and adaptive learning systems.",
        "description_ar": "يركز على تقنيات التعلم بمساعدة الحاسوب (CAL)، بما في ذلك منصات التعلم الإلكتروني، والتدريس المدعوم بالذكاء الاصطناعي، وأنظمة التعلم التكيفية."
    },
    "Adv DB": {
        "arabic_name": "قواعد البيانات المتقدمة",
        "description_en": "Covers advanced database concepts such as distributed databases, NoSQL databases, big data storage, and cloud-based database solutions.",
        "description_ar": "يغطي مفاهيم قواعد البيانات المتقدمة مثل قواعد البيانات الموزعة، قواعد بيانات NoSQL، تخزين البيانات الضخمة، وحلول قواعد البيانات المستندة إلى السحابة."
    },
    "Multimedia": {
        "arabic_name": "الوسائط المتعددة",
        "description_en": "Introduces multimedia systems, digital media processing, interactive media applications, and compression techniques.",
        "description_ar": "يقدم أنظمة الوسائط المتعددة، ومعالجة الوسائط الرقمية، وتطبيقات الوسائط التفاعلية، وتقنيات الضغط."
    },
    "GIS": {
        "arabic_name": "نظم المعلومات الجغرافية",
        "description_en": "Explores Geographic Information Systems (GIS), spatial data analysis, remote sensing, and geospatial visualization.",
        "description_ar": "يستكشف نظم المعلومات الجغرافية (GIS)، وتحليل البيانات المكانية، والاستشعار عن بعد، وتصور البيانات الجغرافية."
    },
    "Image": {
        "arabic_name": "معالجة الصور",
        "description_en": "Covers image processing techniques, including image filtering, edge detection, object recognition, and computer vision applications.",
        "description_ar": "يغطي تقنيات معالجة الصور، بما في ذلك ترشيح الصور، واكتشاف الحواف، والتعرف على الكائنات، وتطبيقات الرؤية الحاسوبية."
    },
    "Adv Software": {
        "arabic_name": "هندسة البرمجيات المتقدمة",
        "description_en": "Focuses on advanced software engineering methodologies, including agile development, DevOps practices, and software architecture design.",
        "description_ar": "يركز على منهجيات هندسة البرمجيات المتقدمة، بما في ذلك التطوير السريع (Agile)، ممارسات DevOps، وتصميم هندسة البرمجيات."
    }
}
