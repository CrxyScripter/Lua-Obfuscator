local YourFileGoesHere = [[
--SCRIPT
]]

local Called = require("module/obfuscate")

Called:Obfuscate({
  Watermark = "// Obfuscated with Lua Obfuscator",
  VariableCom = "Trying to De-Obfuscate?",
  EncryptVarCom = true,
  VariableName = "LuaObfuscator",
  Script = YourFileGoesHere
})