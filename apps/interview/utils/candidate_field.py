default_fieldsets = (
    ('基本信息', {'fields': (
        ('username', 'gender', 'phone'),
        ('email', 'apply_position', 'school'),
        ('city', 'major', 'degree'),
        ('paper_score',)
    )}),
    ('一面信息', {'fields': (
        ('first_score', 'first_learning_ability', 'first_professional_competency'),
        ('first_advantage', 'first_disadvantage', 'first_result'),
        ('first_interviewer_user', 'first_remark')
    )}),
    ('二面信息', {'fields': (
        ('second_score', 'second_professional_competency', 'second_advantage'),
        ('second_disadvantage', 'second_result'),
        ('second_interviewer_user', 'second_remark')
    )}),
    ('HR信息', {'fields': (
        ('hr_score', 'hr_result'),
        ('hr_interviewer_user', 'hr_remark', 'creator'),
        ('last_editor',)
    )})
)

default_fieldsets_first = (
    ('基本信息', {'fields': (
        ('username', 'gender', 'phone'),
        ('email', 'apply_position', 'school'),
        ('city', 'major', 'degree'),
        ('paper_score',)
    )}),
    ('一面信息', {'fields': (
        ('first_score', 'first_learning_ability', 'first_professional_competency'),
        ('first_advantage', 'first_disadvantage', 'first_result'),
        ('first_interviewer_user', 'first_remark')
    )})
)

default_fieldsets_second = (
    ('基本信息', {'fields': (
        ('username', 'gender', 'phone'),
        ('email', 'apply_position', 'school'),
        ('city', 'major', 'degree'),
        ('paper_score',)
    )}),
    ('一面信息', {'fields': (
        ('first_score', 'first_learning_ability', 'first_professional_competency'),
        ('first_advantage', 'first_disadvantage', 'first_result'),
        ('first_interviewer_user', 'first_remark')
    )}),
    ('二面信息', {'fields': (
        ('second_score', 'second_professional_competency', 'second_advantage'),
        ('second_disadvantage', 'second_result'),
        ('second_interviewer_user', 'second_remark')
    )})
)
