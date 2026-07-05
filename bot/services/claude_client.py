from groq import AsyncGroq
from config import GROQ_API_KEY, GROQ_MODEL

SYSTEM_PROMPT = (
    "You are an experienced senior software developer. "
    "Be specific, concise and practical. "
    "Use emoji to structure your response."
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
            f"Do a code review of this {lang} code.\n\n"
            f"```{lang}\n{code}\n```\n\n"
            "Find:\n"
            "🐛 Bugs and errors\n"
            "⚠️ Potential issues\n"
            "🔒 Security problems\n"
            "💡 Concrete fix suggestions"
        )

    async def explain_code(self, code: str, lang: str) -> str:
        return await self._ask(
            f"Explain this {lang} code in simple terms.\n\n"
            f"```{lang}\n{code}\n```\n\n"
            "Structure your answer:\n"
            "📌 What the code does overall\n"
            "🔍 How it works step by step\n"
            "📦 What libraries/patterns it uses"
        )

    async def optimize_code(self, code: str, lang: str) -> str:
        return await self._ask(
            f"Optimize this {lang} code.\n\n"
            f"```{lang}\n{code}\n```\n\n"
            "Focus on:\n"
            "⚡ Performance\n"
            "📖 Readability\n"
            "🏗️ Structure and best practices\n\n"
            "Provide the improved version with an explanation of changes."
        )

    async def improve_code(self, code: str, lang: str) -> str:
        return await self._ask(
            f"Improve this {lang} code.\n\n"
            f"```{lang}\n{code}\n```\n\n"
            "Provide:\n"
            "✨ Improved version\n"
            "📝 What you changed and why"
        )


# single instance shared across all handlers
groq_client = ClaudeClient()
