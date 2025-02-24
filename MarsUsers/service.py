from asgiref.sync import sync_to_async
from .models import Xodimlar, ExcelModel
from Core.settings import BASE_DIR
import openpyxl


@sync_to_async
def finance_service(user_id):
    user = Xodimlar.objects.filter(user_id=user_id).first()
    last_excel = ExcelModel.objects.all().order_by('-id').first()

    if user:
        try:
            wb = openpyxl.load_workbook(f"{BASE_DIR}/{last_excel.file}")
            sheet = wb.active

            # Excel faylidagi ustun nomlarini olish (1-qator)
            header = [cell.value for cell in sheet[1]]

            user_data = None
            for row in sheet.iter_rows(min_row=2, values_only=True):  # 2-qatordan boshlab tekshiramiz
                if row[0] == user.full_name:  # Agar FIO mos kelsa, barcha ma'lumotlarni olish
                    user_data = row
                    break

            wb.close()

            if user_data:
                formatted_data = "\n".join(
                    [f"{label}: {value}" for label, value in zip(header, user_data) if value not in [None, ""]]
                )
                return f"Ma'lumotlar:\n{formatted_data}"
            else:
                return "Sizning ma'lumotingiz topilmadi"

        except Exception as e:
            return f"Xatolik yuz berdi: {str(e)}"

    return "Foydalanuvchi topilmadi"
