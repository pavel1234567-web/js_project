import json
import shutil
from pathlib import Path
from django.conf import settings
from django.core.management.base import BaseCommand
from portfolio.models import Product

class Command(BaseCommand):
    help = "Экспорт товаров в products.js"

    def handle(self, *args, **kwargs):
        SITE_DIR = Path(settings.BASE_DIR)  # корень проекта
        JS_FILE = SITE_DIR / "public" / "js" / "products.js"
        IMG_DIR = SITE_DIR / "public" / "img" / "products"
        # IMG_DIR = SITE_DIR / "media"  / "products"
        JS_FILE.parent.mkdir(parents=True, exist_ok=True)
        IMG_DIR.mkdir(parents=True, exist_ok=True)

        products_list = []

        for p in Product.objects.all():
            image_path = "no-image.png"
            if p.image:
                src = Path(p.image.path)
                if src.exists():
                    dest = IMG_DIR / src.name
                    if not dest.exists():
                        shutil.copy2(src, dest)
                    # image_path = f"../public/img/products/{src.name}"
                    image_path = f"public/img/products/{src.name}"
                    # image_path = f"media/products/{src.name}"
                    

            products_list.append({
                "id": p.id,
                "name": p.name,
                "price": float(p.price),
                "article": p.article,
                "image": image_path,
                "category": p.category.name if p.category else "",
                "description": p.description
            })

        content = f"const products = {json.dumps(products_list, indent=2, ensure_ascii=False)};\n\nexport default products;"

        with open(JS_FILE, "w", encoding="utf-8") as f:
            f.write(content)

        self.stdout.write(self.style.SUCCESS("✔ products.js успешно обновлён"))
