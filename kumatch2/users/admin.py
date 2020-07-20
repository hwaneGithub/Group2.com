from django.contrib import admin
from .models import User, Board
# Register your models here.


admin.site.register(User)
@admin.register(Board)

class ArticleAdmin(admin.ModelAdmin):
	list_display = ('id', 'b_title', 'b_writer', 'date_created')  # date_created는 아래 정의한 메소드
	list_display_links = ('id', 'b_title')                      # 상세페이지로 이동할 수 있는 필드 리스트

	def date_created(self, obj):                              # create_at 필드의 출력형식을 변경해주는 메소드
		return obj.b_date.strftime("%Y-%m-%d")

	date_created.admin_order_field = 'b_date'             # date_created 컬럼 제목을 클릭시 실제 어떤 데이터를 기준으로 정렬할 지 결정
	date_created.short_description = '작성일'