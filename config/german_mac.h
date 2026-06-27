/*
 * German keycodes for a macOS host set to the German ("Deutsch") layout.
 *
 * ZMK always sends US-HID key positions; macOS (German) translates them into
 * German characters. The letter / umlaut / shifted-number-row mappings are the
 * same as on German-PC, BUT the AltGr (Option) symbols and the dead keys
 * (^ ~ `) are macOS-specific and differ from a German-PC layout.
 *
 *   AltGr == the Option (Alt) key on macOS -> RA() / right-Option here.
 *   Dead keys (^ ~ `) are produced as macros in the keymap (accent + space).
 */
#pragma once

/* ---- Letters: QWERTY arrangement on a German OS -------------------------- *
 * macOS-German swaps Y<->Z; we cancel that so the board stays QWERTY (Y on the
 * top row, Z bottom-left), matching the old Defiant. For true QWERTZ, delete
 * the two swap lines below.                                                   */
#define GE_A A
#define GE_B B
#define GE_C C
#define GE_D D
#define GE_E E
#define GE_F F
#define GE_G G
#define GE_H H
#define GE_I I
#define GE_J J
#define GE_K K
#define GE_L L
#define GE_M M
#define GE_N N
#define GE_O O
#define GE_P P
#define GE_Q Q
#define GE_R R
#define GE_S S
#define GE_T T
#define GE_U U
#define GE_V V
#define GE_W W
#define GE_X X
#define GE_Y Z   // type 'y'  (German OS would otherwise read US-Y as 'z')
#define GE_Z Y   // type 'z'

/* ---- Umlauts & sharp-s (identical PC/Mac) -------------------------------- */
#define GE_UE     LBKT          // ü   ( Ü = LS(LBKT) )
#define GE_OE     SEMI          // ö   ( Ö = LS(SEMI) )
#define GE_AE     SQT           // ä   ( Ä = LS(SQT)  )
#define GE_ESZETT MINUS         // ß

/* ---- Punctuation & shifted number row (identical PC/Mac) ----------------- */
#define GE_EXCLAIM    LS(N1)    // !
#define GE_DQUOTE     LS(N2)    // "
#define GE_SECTION    LS(N3)    // §
#define GE_DOLLAR     LS(N4)    // $
#define GE_PRCNT      LS(N5)    // %
#define GE_AMPS       LS(N6)    // &
#define GE_FSLH       LS(N7)    // /
#define GE_LPAREN     LS(N8)    // (
#define GE_RPAREN     LS(N9)    // )
#define GE_EQUAL      LS(N0)    // =
#define GE_QUESTION   LS(MINUS) // ?
#define GE_PLUS       RBKT      // +
#define GE_STAR       LS(RBKT)  // *
#define GE_HASH       BSLH      // #
#define GE_APS        LS(BSLH)  // '   (apostrophe)
#define GE_COMMA      COMMA     // ,
#define GE_SEMICOLON  LS(COMMA) // ;
#define GE_DOT        DOT       // .
#define GE_COLON      LS(DOT)   // :
#define GE_MINUS      SLASH     // -
#define GE_UNDERSCORE LS(SLASH) // _
#define GE_LT         NON_US_BSLH      // <
#define GE_GT         LS(NON_US_BSLH)  // >

/* ---- AltGr / Option symbols: macOS-German SPECIFIC (differ from PC!) ------ */
#define GE_AT         RA(L)        // @   ⌥L
#define GE_EURO       RA(E)        // €   ⌥E
#define GE_LBRACE     RA(N8)       // {   ⌥8
#define GE_RBRACE     RA(N9)       // }   ⌥9
#define GE_LBRACKET   RA(N5)       // [   ⌥5
#define GE_RBRACKET   RA(N6)       // ]   ⌥6
#define GE_PIPE       RA(N7)       // |   ⌥7
#define GE_BACKSLASH  RA(LS(N7))   // \   ⌥⇧7

/* ---- Dead keys: produced via macros in the keymap (accent + SPACE) -------- *
 *   ^  ->  GRAVE      then SPACE   (de_caret)
 *   `  ->  LS(EQUAL)  then SPACE   (de_grave)
 *   ~  ->  RA(N)      then SPACE   (de_tilde)   // verify ⌥N on your Mac
 * These are dead accents on German-macOS, so a trailing SPACE emits the bare
 * character. Adjust if your macOS version maps them differently.             */
