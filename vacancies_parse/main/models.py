from django.db import models

# Модель для хранения статистики с HTML-таблицей и графиком
class GeneralStatistics(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название раздела")
    html_table = models.TextField(verbose_name="HTML таблица")  # Сохраняем HTML-код таблицы
    graph_image = models.ImageField(upload_to="graphs/", null=True, blank=True, verbose_name="График (PNG)")  # График

    objects = models.Manager()

    class Meta:
        verbose_name = "Раздел статистики"
        verbose_name_plural = "Разделы статистики"

    def __str__(self):
        return self.title


class DemandStatistics(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название раздела")
    html_table = models.TextField(verbose_name="HTML таблица")  # Сохраняем HTML-код таблицы
    graph_image = models.ImageField(upload_to="graphs/", null=True, blank=True, verbose_name="График (PNG)")  # График

    objects = models.Manager()

    class Meta:
        verbose_name = "Статистика востребованности"
        verbose_name_plural = "Статистика востребованности"

    def __str__(self):
        return self.title