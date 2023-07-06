from django.db import models

# Create your models here.

# 데이터	                            유형	                             설명
# id	                                String	                            큐브 사용 내역에 대한 고유 식별자
# character_name	                    String	                            캐릭터이름 
# create_date	                        String	                            큐브 사용 날짜
# cube_type	                            String	                            사용한 큐브
# item_upgrade_result	                String	                            큐브 사용 결과(등업 결과)
# miracle_time_flag	                    String	                            미라클 타임 적용 여부
# item_equip_part	                    String	                            장비 분류
# item_level	                        integer	                            장비 레벨
# target_item	                        String	                            큐브를 사용한 장비
# potential_option_grade	            String	                            잠재능력 등급
# additional_potential_option_grade	    String	                            에디셔널 잠재능력 등급
# upgradeguarantee	                    Boolean	                            천장에 도달하여 확정 등급 상승한 여부
# upgradeguaranteecount	                Integer	                            현재까지 쌓은 스택
# before_potential_options	            object array(CubeResultOptionDTO)	큐브사용전 잠재능력 옵션
# before_additional_potential_options	object array(CubeResultOptionDTO)	큐브사용전 에디셔널 잠재능력 옵션
# after_potential_options	            object array(CubeResultOptionDTO)	큐브 사용 후 잠재능력 옵션
# after_additional_potential_options	object array(CubeResultOptionDTO)	큐브 사용 후 에디셔널 잠재능력 옵션
# value                                 string                              옵션이름
# grade                                 string                              옵션등급

class Cube(models.Model):
    idx = models.AutoField(primary_key=True)
    key = models.TextField(null=False,blank=False) # API Key
    character_name = models.CharField(max_length=12) # 캐릭닉넴
    create_date = models.DateTimeField() # 사용한 날짜
    cube_type = models.CharField(max_length=12) # 큐브 종류
    item_upgrade_result = models.CharField(max_length=12) # 등업결과
    item_level = models.IntegerField() # 아이템 레벨
    target_item = models.CharField(max_length=20) # 아이템 이름
    potential_option_grade = models.CharField(max_length=4) # 위잠등급
    before_options_value1 = models.CharField(max_length=30)
    before_options_grade1 = models.CharField(max_length=4)
    before_options_value2 = models.CharField(max_length=30)
    before_options_grade2 = models.CharField(max_length=4)
    before_options_value3 = models.CharField(max_length=30)
    before_options_grade3 = models.CharField(max_length=4)
    after_options_value1 = models.CharField(max_length=30)
    after_options_grade1 = models.CharField(max_length=4)
    after_options_value2 = models.CharField(max_length=30)
    after_options_grade2 = models.CharField(max_length=4)
    after_options_value3 = models.CharField(max_length=30)
    after_options_grade3 = models.CharField(max_length=4)

    class Meta:
        db_table = 'Cube'