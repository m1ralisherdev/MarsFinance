from asgiref.sync import sync_to_async
from .models import Xodimlar,ExcelModel
from Core.settings import BASE_DIR

# @sync_to_async
# def finance_service(user_id):
#     user = Xodimlar.objects.filter(user_id=user_id).first()
#     excel_file = ExcelModel.objects.all().order_by('-id').first()
#     print(excel_file.file)
#
#
#     return user

import openpyxl

from asgiref.sync import sync_to_async
from .models import Xodimlar, ExcelModel
import openpyxl


@sync_to_async
def finance_service(user_id):
    user = Xodimlar.objects.filter(user_id=user_id).first()
    last_excel = ExcelModel.objects.all().order_by('-id').first()

    if user:
        try:
            wb = openpyxl.load_workbook(f"{BASE_DIR}/{last_excel.file}")
            sheet = wb.active

            LABELS = [
                "ФИО",
                "Фикса",
                "Премия и надбавки",
                "Отпускной",
                "Бальничный",
                "Сокращение",
                "Декрет",
                "Начислено",
                "НДФЛ",
                "ИНПС",
                "Оплачено"
            ]

            user_data = None
            for row in sheet.iter_rows(min_row=1):
                if row[0].value == user.full_name:
                    user_data = [cell.value for cell in row]
                    break

            wb.close()

            if user_data:
                formatted_data = "\n".join([
                    f"{i + 1}. {label}: {value}"
                    for i, (label, value) in enumerate(zip(LABELS, user_data))
                ])
                return f"Ma'lumotlar:\n{formatted_data}"
            else:
                return "Sizning ma'lumotingiz topilmadi"

        except Exception as e:
            return f"Xatolik yuz berdi: {str(e)}"

    return "Foydalanuvchi topilmadi"