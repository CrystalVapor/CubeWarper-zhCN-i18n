//Checks if command blocks are enabled

function commandBlocksEnabled(server) {
  try {
    return server.isCommandBlockEnabled()
  } catch (e) {
    console.error('Could not read command block setting: ' + e)
    return true
  }
}

const WARNING = [
  Text.red("⚠ 此服务器已禁用命令方块。⚠（⚠ Command blocks are disabled on this server. ⚠）").bold(),
  Text.red("这会使整合包后续流程无法正常运行，请启用命令方块。（This will break the pack down the line, so please enable them.）"),
  Text.red("请在 server.properties 中设置 enable-command-block=true。（Set enable-command-block=true in server.properties.）")
]

ServerEvents.loaded(event => {
  if (!commandBlocksEnabled(event.server)) {
    console.warn('Command blocks are DISABLED (enable-command-block=false)')
  }
})

PlayerEvents.loggedIn(event => {
  if (!commandBlocksEnabled(event.server)) {
    event.server.scheduleInTicks(60, () => {
      WARNING.forEach(line => event.player.tell(line))
    })
  }
})