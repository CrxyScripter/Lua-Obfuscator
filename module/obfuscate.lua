local Called = {}
local Options = {
  Comment = "// Obfuscated with Lua Obfuscator",
  Variable_Comment = "IllIlIlIlIlIlIl", 
  Crypt_Var_Comment = true,
  Variable_Name = "LuaObfuscator",
}

local f1 = io.open("module/random/_0xo726421.lua", "w")
local f2 = io.open("module/random/_0xo726422.lua", "w")

f1:write(math.random(1, 500))
f2:write(math.random(1, 500))

f1:close()
f2:close()

local function getmodule()
	local mloaded, module = pcall(function()
		return dofile("module/obfuscate-cli.lua")
	end)
	if not mloaded or module == nil then
		if not mloaded then
			print(module)
		end
		print("Put a path correctly! (ex: C:\\path\\to\\module.lua)")
		return getmodule()
	else
		return module
	end
end
local M_ = getmodule()
if not (M_.crypt ~= nil and type(M_.crypt) == 'function') then
	return nil
end

local function getRfile()
	local mpath = "module/random/_0xo726422.lua"
	local mloaded, f, err = pcall(function()
		return io.open(mpath, "rb")
	end)
	if not mloaded or f == nil then
		if not mloaded then
			print(f)
		end
		print("Put a path correctly! (ex: savetheoof.lua)")
		return getRfile()
	else
		return f
	end
end

local obrfile = getRfile()
local obrcode = "module/random/_0xo726422.lua"
obrfile:close()

local function getWfile()
	local mpath = "module/random/_0xo726421.lua"
	local mloaded, f, err = pcall(function()
		return io.open(mpath, "rb")
	end)
	if not mloaded or f == nil then
		if not mloaded then
			print(f)
		end
		print("Put a path correctly! (ex: soof_obfuscated.lua)")
		return getWfile()
	else
		return f
	end
end

local wfile = getWfile()

local _settings = { 
	comment = Comment,
	variablecomment = Variable_Comment,
	cryptvarcomment = Crypt_Var_Comment,
	variablename = Variable_Name
}

local com_ = Comment
if com_ == "" then
	com_ = Comment
end

local varcom_ = Variable_Comment
if varcom_ == "" then
	varcom_ = Variable_Comment
end

local varnam_ = Variable_Name
if varnam_ == "" then
	varnam_ = Variable_Name
end

local cryvar_ = "y"
local cryyes = true
if cryvar_:lower() == "n" then
	cryyes = false
else
	cryyes = true
end

local options_ = {
	comment = Comment,
	variablecomment = Variable_Comment,
	cryptvarcomment = Crypt_Var_Comment,
	variablename = Variable_Name,
}

function Called:Obfuscate(Option)
  local RealOption = {
    comment = Option.Watermark,
    variablecomment = Option.VariableCom
    cryptvarcomment = Option.EncryptVarCom
    variablename = Option.VariableName
  }
  
  local memoryleakerlolwhat = M_(Option.Script, RealOption)

  wfile:write(memoryleakerlolwhat)
  wfile:close()
  print(memoryleakerlolwhat)

  os.remove("module/random/_0xo726421.lua")
  os.remove("module/random/_0xo726422.lua")
end

return Called