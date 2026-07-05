from groq import AsyncGroq
from config import GROQ_API_KEY, GROQ_MODEL

SYSTEM_PROMPT = (
    "Ти — досвідчений senior розробник. Відповідай українською мовою. "
    "Будь конкретним, стислим і практичним. "
    "Використовуй emoji для структурування відповіді."
)


class ClaudeClient:
    def __init__(self) -> None:
        self._client = AsyncGroq(api_key=GROQ_API_KEY)

    async def _ask(self, prompt: str) -> str:
        response = await self._client.chat.completions.create(
            model=GROQ_MODEL,
            max_tokens=2048,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt},
            ],
        )
        return response.choices[0].message.content

    async def review_code(self, code: str, lang: str) -> str:
        return await self._ask(
            f"Проведи code review цього {lang} коду.\n\n"
            f"```{lang}\n{code}\n```\n\n"
            "Знайди:\n"
            "🐛 Баги та помилки\n"
            "⚠️ Потенційні проблеми\n"
            "🔒 Проблеми безпеки\n"
            "💡 Конкретні пропозиції виправлення"
        )

    async def explain_code(self, code: str, lang: str) -> str:
        return await self._ask(
            f"Поясни цей {lang} код простими словами.\n\n"
            f"```{lang}\n{code}\n```\n\n"
            "Структуруй відповідь:\n"
            "📌 Що робить код загалом\n"
            "🔍 Як працює крок за кроком\n"
            "📦 Які бібліотеки/паттерни використовує"
        )

    async def optimize_code(self, code: str, lang: str) -> str:
        return await self._ask(
            f"Оптимізуй цей {lang} код.\n\n"
            f"```{lang}\n{code}\n```\n\n"
            "Зосередься на:\n"
            "⚡ Продуктивності\n"
            "📖 Читабельності\n"
            "🏗️ Структурі та best practices\n\n"
            "Надай покращену версію коду з поясненням змін."
        )

    async def improve_code(self, code: str, lang: str) -> str:
        return await self._ask(
            f"Покращ цей {lang} код.\n\n"
            f"```{lang}\n{code}\n```\n\n"
            "Запропонуй:\n"
            "✨ Покращену версію\n"
            "📝 Що саме і чому змінив"
        )


# один екземпляр на весь бот
groq_client = ClaudeClient()
