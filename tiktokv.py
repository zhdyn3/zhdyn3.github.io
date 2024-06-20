from tiktok import TikTokApi
import json
import time

# Инициализируем TikTok API
api = TikTokApi()

# Функция для получения популярных видео
def get_popular_videos():
    try:
        # Запрашиваем список популярных видео
        popular_videos = api.trending(count=10)  # Получаем 10 популярных видео (можно изменить количество по желанию)
        
        # Преобразуем объекты видео в формат JSON
        popular_videos_json = [video.dict() for video in popular_videos]
        
        # Сохраняем данные в файл
        with open('popular_videos.json', 'w', encoding='utf-8') as f:
            json.dump(popular_videos_json, f, ensure_ascii=False, indent=4)
            
        print("Данные о популярных видео успешно сохранены в popular_videos.json")
    
    except Exception as e:
        print(f"Произошла ошибка при получении популярных видео: {str(e)}")

# Запускаем функцию для получения популярных видео
get_popular_videos()
