import csv
from django.core.management import BaseCommand
from apps.interview.models import Candidate


class Command(BaseCommand):
    help = '从一个CSV文件的内容中读取候选人列表, 导入到数据库中'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **options):
        path = options['path']
        with open(path, 'rt', encoding='gbk') as f:
            reader = csv.reader(f, dialect='excel', delimiter=',')
            for row in reader:
                candidate = Candidate.objects.create(
                    username=row[0],
                    city=row[1],
                    school=row[2],
                    major=row[3],
                    degree=row[4],
                    paper_score=row[5]
                )
                print(candidate)
