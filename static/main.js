const icon = document.querySelector('#detailsExpander')
function onToggle(){
  icon.name === 'caret-down-outline' ?
 (icon.name = 'caret-up-outline', icon.classList.remove('animate-bounce')) :
 (icon.name = 'caret-down-outline', icon.classList.add('animate-bounce'))
 }