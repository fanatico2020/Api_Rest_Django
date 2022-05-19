from rest_framework import serializers
from .models import Curso,Avaliacao
from django.db.models import Avg

class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email':{'write_only':True}
        }
        model = Avaliacao
        fields = (
            'id',
            'curso',
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo'
        )

        def validate_avaliacao(self,valor):
            if valor in range(1,6): # 1,2,3,4,5
                return valor
            raise serializers.ValidationError('A avaliação precisa ser um inteiro entre 1 e 5')


class CursoSerializer(serializers.ModelSerializer):
    # 1 Nested Relationship
    # avaliacoes = AvaliacaoSerializer(many=True,read_only=True)

    # 2 HyperLinked Related Field
    """
    avaliacoes = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='avaliacao-detail'
    )
    """

    # 3 Primery Key Related Field
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True,read_only=True)

    media_avaliacoes = serializers.SerializerMethodField()

    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes',
            'media_avaliacoes'
        )


    def get_media_avaliacoes(self,obj):
        media = obj.avaliacoes.aggregate(Avg('avaliacao')).get('avaliacao__avg')

        if media is None:
            return 0
        return round(media * 2 ) / 2