// to play the sound effects
var DROP_SOUND = new buzz.sound([
    "/static/drop.mp3"
]);
var MOVE_SOUND = new buzz.sound([
    "/static/move.mp3"
]);
var ROTATE_SOUND = new buzz.sound([
    "/static/rotate.mp3"
]);
var OVERLAP_SOUND = new buzz.sound([
    "/static/overlap.mp3"
]);

var GROUP_SOUND = new buzz.group([ DROP_SOUND, MOVE_SOUND, ROTATE_SOUND, OVERLAP_SOUND ]);

function isAvailableSound() {
	return !($("#sound").css("display") === "none");
}
function loadAllSound() {
	if ( isAvailableSound() ) GROUP_SOUND.load();
}
function stopAllSound() {
	if (isAvailableSound()) {
		GROUP_SOUND.stop();
	}
}
function muteAllSound() {
	if (isAvailableSound()) {
		GROUP_SOUND.mute();
	}
}
function unmuteAllSound() {
	if (isAvailableSound()) {
		GROUP_SOUND.unmute();
	}
}

function playDropSound() {
	if ( isAvailableSound() ) {
		ROTATE_SOUND.stop();
		MOVE_SOUND.stop();
		DROP_SOUND.stop();
		DROP_SOUND.play();
	}
}
function playMoveSound() {
	if ( isAvailableSound() ) {
		MOVE_SOUND.stop();
		MOVE_SOUND.play();
	}
}
function playRotateSound() {
	if ( isAvailableSound() ) {
		ROTATE_SOUND.stop();
		ROTATE_SOUND.play();
	}
}
function playOverlapSound() {
	if ( isAvailableSound() ) {
    ROTATE_SOUND.stop();
		MOVE_SOUND.stop();
		DROP_SOUND.stop();
    OVERLAP_SOUND.stop();
		OVERLAP_SOUND.play();
	}
}
