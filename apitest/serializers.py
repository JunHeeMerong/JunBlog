from rest_framework import serializers
from apitest.models import Cube, Addcube

class CubeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cube
        fields = ['id', 'character_name', 'create_date', 'cube_type', 'item_upgrade_result','item_level',
                  'target_item','potential_option_grade','before_options_value1','before_options_grade1',
                  'before_options_value2','before_options_grade2','before_options_value3','before_options_grade3',
                  'after_options_value1','after_options_grade1','after_options_value2','after_options_grade2',
                  'after_options_value3','after_options_grade3']