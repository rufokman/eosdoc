from django.db import models


class Queries(models.Model):
    url = models.CharField(max_length=3000, verbose_name='Введите ссылку на документ')
    format = models.PositiveIntegerField(verbose_name='Выберите формат документа',
                                         choices=((0, 'MicrosoftOffice (.docx)'),
                                                  (1, 'LibreOffice (.odt)')
                                                  ),
                                         default=0
                                         )
    time_create = models.DateTimeField(auto_now_add=True)
    status = models.PositiveIntegerField(default=0)

    class Meta:
        managed = True
        db_table = "queries"
