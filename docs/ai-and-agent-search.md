# AI and agent search

The [Gemini query list](../google-dorks-for-gemini.txt) searches for public pages containing Gemini API configuration names, code markers, or system-instruction fields. Google documents `GEMINI_API_KEY` and `GOOGLE_API_KEY` as environment variable names in its [Gemini API key guide](https://ai.google.dev/gemini-api/docs/api-key). A matching name is not proof that a usable key is exposed. Google also documents `system_instruction` in its [API examples](https://ai.google.dev/gemini-api/docs/generate-content/text-generation).

The [AI-agent list](../google-dorks-for-ai-agents.txt) looks for public agent instructions and configuration formats. A public `AGENTS.md`, prompt template, or tool configuration may be intentional. Review its context and the owner's policy before treating it as a finding.

Use Google Search for these queries; Gemini is the technology being searched for, not a separate search operator. Apply the [scoping and reporting guidance](safe-use.md). Do not ask an AI model to invent a vulnerability or submit its unverified output as a dork. When AI helps draft a contribution, check the syntax, the product terminology, false positives, and the source yourself.

Potential future additions should be driven by verified examples: model configuration exposure, public agent tool manifests, and defensive checks for indexed prompt or retrieval data. Keep each category small until its usefulness is demonstrated.
