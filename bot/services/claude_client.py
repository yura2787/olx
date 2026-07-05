import anthropic
from config import ANTHROPIC_API_KEY, CLAUDE_MODEL

SYSTEM_PROMPT = (
    "Ти — досвідчений senior розробник. Відповідай українською мовою. "
    "Будь конкретним, стислим і практичним. "
    "Використовуй emoji для структурування відповіді."
)


class ClaudeClient:
    def __init__(self) -> None:
        self._client = anthropic.AsyncAnthropic(api_key=ANTHROPIC_API_KEY)

    async def _ask(self, prompt: str) -> str:
        message = await self._client.messages.create(
            model=CLAUDE_MODEL,
            max_tokens=2048,
            system=SYSTEM_PROMPT,
            messages=[{"role": "user", "content": prompt}],
        )
        return message.content[0].text

    async def review_code(self, code: str, lang: str) -> str:
        prompt = (
            f"Проведи code review цього {lang} коду.\n\n"
            f"```{lang}\n{code}\n```\n\n"
            "Знайди:\n"
            "🐛 Баги та помилки\n"
            "⚠️ Потенційні проблеми\n"
            "🔒 Проблеми безпеки\n"
            "💡 Конкретні пропозиції виправлення"
        )
        return await self._ask(prompt)

    async def explain_code(self, code: str, lang: str) -> str:
        prompt = (
            f"Поясни цей {lang} код простими словами.\n\n"
            f"```{lang}\n{code}\n```\n\n"
            "Структуруй відповідь:\n"
            "📌 Що робить код загалом\n"
            "🔍 Як працює крок за кроком\n"
            "📦 Які бібліотеки/паттерни використовує"
        )
        return await self._ask(prompt)

    async def optimize_code(self, code: str, lang: str) -> str:
        prompt = (
            f"Оптимізуй цей {lang} код.\n\n"
            f"```{lang}\n{code}\n```\n\n"
            "Зосередься на:\n"
            "⚡ Продуктивності\n"
            "📖 Читабельності\n"
            "🏗️ Структурі та best practices\n\n"
            "Надай покращену версію коду з поясненням змін."
        )
        return await self._ask(prompt)

    async def improve_code(self, code: str, lang: str) -> str:
        prompt = (
            f"Покращ цей {lang} код.\n\n"
            f"```{lang}\n{code}\n```\n\n"
            "Запропонуй:\n"
            "✨ Покращену версію\n"
            "📝 Що саме і чому змінив"
        )
        return await self._ask(prompt)
