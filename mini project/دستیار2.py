import pyttsx3
import speech_recognition as sr
import wikipedia

# تنظیم موتور تبدیل متن به گفتار
engine = pyttsx3.init()

# تنظیم شناسه زبان به فارسی
engine.setProperty('rate', 150)  # تنظیم سرعت گفتار (اختیاری)


# تابع برای تبدیل متن به گفتار
def text_to_speech(text):
    engine.say(text)
    engine.runAndWait()


# تابع برای تشخیص و پاسخ به گفتار
def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("گوش کنید ...")
        audio = r.listen(source)
    try:
        print("در حال تشخیص ...")
        query = r.recognize_google(audio, language='fa-IR')
        print(f"شما گفته اید: {query}")
        return query
    except Exception as e:
        print("متوجه نشدم. لطفا دوباره تلاش کنید.")
        return ""


# تابع برای جستجو در ویکیپدیا و نمایش نتیجه
def search_wikipedia(query, wikipedia=None):
    wiki_wiki = wikipedia.Wikipedia('fa')  # تنظیم زبان به فارسی
    page_py = wiki_wiki.page(query)
    if page_py.exists():
        print("نتیجه:")
        print(page_py.summary[:200])  # نمایش خلاصه مقاله
        text_to_speech(page_py.summary[:200])  # تبدیل خلاصه مقاله به گفتار
    else:
        print("هیچ نتیجه‌ای یافت نشد.")


# برنامه اصلی
def main():
    while True:
        print("گفتار خود را ضبط کنید:")
        query = speech_to_text()
        if query:
            if "جستجو" in query:
                query = query.replace("جستجو", "").strip()
                search_wikipedia(query)
            elif "خروج" in query:
                print("خدانگهدار!")
                break


if __name__ == '__main__':
    main()
