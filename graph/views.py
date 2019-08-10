import os
import time
import random
import datetime

from django.conf import settings
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.serializers import ValidationError

from .serializer import UploadImageSerializer


upload_dir = getattr(settings, 'GG_UPLOAD_DIR')
graph_max_size = getattr(settings, 'GG_GRAPH_MAX_SIZE')

if not upload_dir:
    raise Exception('请在settings中配置GG_UPLOAD_DIR以确定文件上传后的存储位置')

if not graph_max_size:
    raise Exception('请在settings中配置GG_GRAPH_MAX_SIZE以确定文件上传的大小限制')


class GraphView(APIView):

    def build_file_full_path(self, file):
        """构造文件路径"""
        now = datetime.datetime.now()
        file_path = '{}{}{}'.format(
            upload_dir,
            '' if upload_dir[-1] == '/' else '/',
            '{}/{}/{}/'.format(
                now.strftime('%Y'),
                now.strftime('%m'),
                now.strftime('%d'),
            ),
        )
        os.makedirs(file_path, exist_ok=True)
        return '{}/{}'.format(
            file_path,
            '{}_{}'.format(now.strftime('%s'), file.name)
        )

    def save_file(self, file):
        """存储文件"""
        file_full_path = self.build_file_full_path(file)

        while os.path.exists(file_full_path):
            time.sleep(0.001 * random.randint(1, 3))
            file_full_path = self.build_file_full_path(file)

        with open(file_full_path, 'wb') as f:
            f.write(file.read())

        scheme = self.request.scheme
        host = self.request.get_host()
        domain = '{}://{}'.format(scheme, host)
        return '{}{}'.format(domain, file_full_path)

    def judge_file_size(self, file):
        if file.size <= graph_max_size:
            return True
        else:
            raise ValidationError('文件大小超出限制')

    def post(self, request):
        serializer = UploadImageSerializer(data=request.data)
        if serializer.is_valid():   # 判断用户名密码有效性
            file = request.FILES.get('graph')
            url = self.save_file(file)
            self.judge_file_size(file)
            return JsonResponse({'url': url})
        else:
            return JsonResponse(serializer.errors)

