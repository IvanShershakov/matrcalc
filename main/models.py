# from django.db import models, DecimalField
# from django.contrib.postgres.fields import ArrayField
#
#
# class Matrix(models.Model):
#     row = DecimalField('Строки', default=3)
#     col = DecimalField('Столбцы', default=3)
#     data = ArrayField(
#         ArrayField(
#             models.DecimalField('field'),
#             size=row,
#         ),
#         size=col,
#     )
#
#     def __str__(self):
#         return (self.row, self.col)