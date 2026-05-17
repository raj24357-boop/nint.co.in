<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>NINT.co.in – India's Live News Portal</title>
<meta name="description" content="NINT – National India News Today. Breaking news, Politics, Sports, Telugu, World, Business, Student Zone. Live, AI-powered, refreshed every 5 minutes.">
<meta name="keywords" content="India news, Telugu news, breaking news, NINT, politics, sports, UPSC, NEET, JEE, EAMCET">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;0,900;1,400;1,700&family=Source+Serif+4:ital,opsz,wght@0,8..60,300;0,8..60,400;0,8..60,600;1,8..60,300;1,8..60,400&family=Noto+Sans+Telugu:wght@400;600;700&family=Barlow+Condensed:wght@400;600;700;800&display=swap" rel="stylesheet">

<!-- Google AdSense -->
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-XXXXXXXXXXXXXXXX" crossorigin="anonymous"></script>

<style>
:root {
  --crimson: #C8102E;
  --crimson-dark: #9A0B22;
  --navy: #0D1B2A;
  --navy-mid: #1A2E40;
  --gold: #D4AF37;
  --gold-light: #F0D060;
  --cream: #FAF7F2;
  --cream-dark: #F0EBE1;
  --ink: #1A1108;
  --ink-mid: #3D3020;
  --ink-light: #6B5C48;
  --rule: #DDD5C8;
  --rule-dark: #C0B49E;
  --white: #FFFFFF;
  --green: #1A7A3C;
  --red-ticker: #B80020;
  --breaking-bg: #C8102E;
  --shadow-sm: 0 1px 4px rgba(0,0,0,.10);
  --shadow-md: 0 4px 16px rgba(0,0,0,.13);
  --shadow-lg: 0 8px 32px rgba(0,0,0,.18);
}

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html { scroll-behavior: smooth; }

body {
  font-family: 'Source Serif 4', Georgia, serif;
  background: var(--cream);
  color: var(--ink);
  font-size: 15px;
  line-height: 1.6;
  min-height: 100vh;
}

/* ── BREAKING TICKER ── */
.ticker-bar {
  background: var(--crimson);
  color: #fff;
  display: flex;
  align-items: center;
  overflow: hidden;
  height: 34px;
  position: sticky;
  top: 0;
  z-index: 100;
  box-shadow: 0 2px 8px rgba(0,0,0,.25);
}
.ticker-label {
  background: var(--navy);
  color: var(--gold);
  font-family: 'Barlow Condensed', sans-serif;
  font-weight: 800;
  font-size: 12px;
  letter-spacing: 2px;
  text-transform: uppercase;
  padding: 0 14px;
  height: 100%;
  display: flex;
  align-items: center;
  white-space: nowrap;
  flex-shrink: 0;
  border-right: 2px solid var(--gold);
}
.ticker-label span { animation: blink 1.2s infinite; }
@keyframes blink { 0%,100%{opacity:1} 50%{opacity:.3} }
.ticker-track {
  flex: 1;
  overflow: hidden;
  position: relative;
  height: 100%;
  display: flex;
  align-items: center;
}
.ticker-inner {
  display: flex;
  white-space: nowrap;
  animation: ticker 60s linear infinite;
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 14px;
  font-weight: 600;
  letter-spacing: .3px;
}
.ticker-inner span {
  padding: 0 40px;
  border-right: 1px solid rgba(255,255,255,.3);
}
@keyframes ticker {
  0% { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}

/* ── TOP AD BAR ── */
.top-ad {
  background: var(--cream-dark);
  border-bottom: 1px solid var(--rule);
  text-align: center;
  padding: 6px 0;
  font-size: 11px;
  color: var(--ink-light);
  letter-spacing: .5px;
}
.ad-slot {
  background: #e8e2d8;
  border: 1px dashed #b0a898;
  border-radius: 2px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  color: #888;
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 11px;
  letter-spacing: 1px;
}
.ad-slot-leaderboard { width: min(728px, 98vw); height: 90px; }
.ad-slot-rect { width: 300px; height: 250px; }
.ad-slot-banner { width: 100%; height: 60px; }

/* ── MASTHEAD ── */
.masthead {
  background: var(--navy);
  padding: 0;
  border-bottom: 4px solid var(--crimson);
  position: relative;
  overflow: hidden;
}
.masthead::before {
  content: '';
  position: absolute;
  inset: 0;
  background: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23D4AF37' fill-opacity='0.04'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
  pointer-events: none;
}
.masthead-inner {
  max-width: 1280px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 14px 20px 10px;
  gap: 16px;
  flex-wrap: wrap;
}
.masthead-brand {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}
.brand-name {
  font-family: 'Playfair Display', serif;
  font-size: clamp(42px, 8vw, 76px);
  font-weight: 900;
  color: var(--white);
  letter-spacing: -2px;
  line-height: 1;
  text-transform: uppercase;
}
.brand-name em {
  color: var(--gold);
  font-style: normal;
}
.brand-tag {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 3px;
  color: var(--gold);
  text-transform: uppercase;
  margin-top: 2px;
  opacity: .85;
}
.masthead-meta {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 6px;
}
.masthead-date {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 12px;
  font-weight: 600;
  color: rgba(255,255,255,.65);
  letter-spacing: 1px;
  text-transform: uppercase;
}
.refresh-badge {
  display: flex;
  align-items: center;
  gap: 6px;
  background: rgba(255,255,255,.08);
  border: 1px solid rgba(255,255,255,.15);
  border-radius: 20px;
  padding: 4px 12px;
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 12px;
  font-weight: 600;
  color: var(--gold);
  letter-spacing: .5px;
}
.refresh-dot {
  width: 7px; height: 7px;
  background: #4CFF72;
  border-radius: 50%;
  animation: pulse-green 1.4s ease-in-out infinite;
  flex-shrink: 0;
}
@keyframes pulse-green {
  0%,100%{opacity:1;transform:scale(1)} 50%{opacity:.5;transform:scale(1.4)}
}
.live-channels-bar {
  background: var(--navy-mid);
  border-bottom: 1px solid rgba(255,255,255,.08);
}
.live-channels-inner {
  max-width: 1280px;
  margin: 0 auto;
  padding: 6px 20px;
  display: flex;
  align-items: center;
  gap: 8px;
  overflow-x: auto;
  scrollbar-width: none;
}
.live-channels-inner::-webkit-scrollbar { display: none; }
.channel-label {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 2px;
  color: var(--gold);
  text-transform: uppercase;
  flex-shrink: 0;
  margin-right: 4px;
}
.channel-btn {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  background: rgba(255,255,255,.07);
  border: 1px solid rgba(255,255,255,.12);
  color: rgba(255,255,255,.85);
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 12px;
  font-weight: 600;
  letter-spacing: .5px;
  padding: 3px 10px;
  border-radius: 3px;
  cursor: pointer;
  transition: all .2s;
  text-decoration: none;
  white-space: nowrap;
  flex-shrink: 0;
}
.channel-btn:hover {
  background: var(--crimson);
  border-color: var(--crimson);
  color: #fff;
}
.channel-btn .dot {
  width: 5px; height: 5px;
  background: #FF4040;
  border-radius: 50%;
  animation: pulse-green 1s infinite;
}

/* ── NAV ── */
nav.main-nav {
  background: var(--crimson);
  border-bottom: 2px solid var(--crimson-dark);
  position: sticky;
  top: 34px;
  z-index: 90;
}
.nav-inner {
  max-width: 1280px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  overflow-x: auto;
  scrollbar-width: none;
  padding: 0 20px;
}
.nav-inner::-webkit-scrollbar { display: none; }
.nav-link {
  display: block;
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 1.2px;
  text-transform: uppercase;
  color: rgba(255,255,255,.88);
  padding: 10px 14px;
  text-decoration: none;
  white-space: nowrap;
  border-bottom: 3px solid transparent;
  transition: all .18s;
}
.nav-link:hover, .nav-link.active {
  color: var(--gold);
  border-bottom-color: var(--gold);
}
.nav-link.telugu { color: var(--gold-light); }

/* ── LAYOUT ── */
.container { max-width: 1280px; margin: 0 auto; padding: 0 20px; }

.page-grid {
  display: grid;
  grid-template-columns: 1fr 280px;
  gap: 24px;
  padding: 24px 0;
}
@media(max-width: 900px) {
  .page-grid { grid-template-columns: 1fr; }
  .sidebar { display: none; }
}

/* ── SECTION HEADERS ── */
.section-head {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 16px;
  padding-bottom: 8px;
  border-bottom: 3px solid var(--crimson);
}
.section-head h2 {
  font-family: 'Playfair Display', serif;
  font-size: 20px;
  font-weight: 700;
  color: var(--navy);
  line-height: 1;
}
.section-head .tag {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 10px;
  font-weight: 800;
  letter-spacing: 2px;
  text-transform: uppercase;
  background: var(--crimson);
  color: #fff;
  padding: 2px 8px;
  border-radius: 2px;
}
.section-block { margin-bottom: 32px; }

/* ── HERO ── */
.hero-story {
  background: var(--white);
  border: 1px solid var(--rule);
  border-radius: 3px;
  overflow: hidden;
  box-shadow: var(--shadow-md);
  margin-bottom: 24px;
  transition: box-shadow .2s;
}
.hero-story:hover { box-shadow: var(--shadow-lg); }
.hero-img {
  width: 100%;
  height: 340px;
  object-fit: cover;
  display: block;
  background: linear-gradient(135deg, #1A2E40 0%, #C8102E 100%);
  position: relative;
}
.hero-img-placeholder {
  width: 100%;
  height: 340px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: 'Playfair Display', serif;
  font-size: 48px;
  color: rgba(255,255,255,.18);
  background: linear-gradient(135deg, #1A2E40 0%, #0D1B2A 50%, #9A0B22 100%);
  position: relative;
  overflow: hidden;
}
.hero-img-placeholder::after {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(ellipse at 30% 60%, rgba(212,175,55,.10) 0%, transparent 65%);
}
.hero-content { padding: 20px 24px 24px; }
.hero-kicker {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 11px;
  font-weight: 800;
  letter-spacing: 2.5px;
  text-transform: uppercase;
  color: var(--crimson);
  margin-bottom: 8px;
  display: flex;
  align-items: center;
  gap: 8px;
}
.hero-kicker::before {
  content: '';
  display: block;
  width: 20px;
  height: 2px;
  background: var(--crimson);
}
.hero-title {
  font-family: 'Playfair Display', serif;
  font-size: clamp(24px, 4vw, 36px);
  font-weight: 900;
  line-height: 1.18;
  color: var(--navy);
  margin-bottom: 12px;
  cursor: pointer;
}
.hero-title:hover { color: var(--crimson); }
.hero-deck {
  font-size: 15px;
  color: var(--ink-mid);
  line-height: 1.65;
  margin-bottom: 14px;
}
.hero-meta {
  display: flex;
  align-items: center;
  gap: 14px;
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 12px;
  font-weight: 600;
  color: var(--ink-light);
  letter-spacing: .3px;
}
.hero-meta .source { color: var(--crimson); font-weight: 700; }

/* ── CARD GRID ── */
.cards-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  gap: 16px;
}
.news-card {
  background: var(--white);
  border: 1px solid var(--rule);
  border-radius: 3px;
  overflow: hidden;
  box-shadow: var(--shadow-sm);
  transition: all .2s;
  cursor: pointer;
  display: flex;
  flex-direction: column;
}
.news-card:hover {
  box-shadow: var(--shadow-md);
  transform: translateY(-2px);
}
.card-thumb {
  width: 100%;
  height: 160px;
  background: linear-gradient(135deg, var(--navy) 0%, #264059 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 36px;
  flex-shrink: 0;
  position: relative;
  overflow: hidden;
}
.card-thumb::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 40px;
  background: linear-gradient(transparent, rgba(0,0,0,.3));
}
.card-body { padding: 14px 14px 16px; flex: 1; display: flex; flex-direction: column; }
.card-kicker {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 10px;
  font-weight: 800;
  letter-spacing: 2px;
  text-transform: uppercase;
  color: var(--crimson);
  margin-bottom: 6px;
}
.card-title {
  font-family: 'Playfair Display', serif;
  font-size: 16px;
  font-weight: 700;
  line-height: 1.35;
  color: var(--navy);
  margin-bottom: 8px;
  flex: 1;
}
.card-meta {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 11px;
  font-weight: 600;
  color: var(--ink-light);
  margin-top: auto;
  letter-spacing: .2px;
}

/* ── TOP 5 LIST ── */
.top5-list { display: flex; flex-direction: column; gap: 0; }
.top5-item {
  display: flex;
  gap: 14px;
  align-items: flex-start;
  padding: 14px 0;
  border-bottom: 1px solid var(--rule);
  cursor: pointer;
  transition: background .15s;
}
.top5-item:last-child { border-bottom: none; }
.top5-item:hover { background: rgba(200,16,46,.03); }
.top5-num {
  font-family: 'Playfair Display', serif;
  font-size: 38px;
  font-weight: 900;
  color: var(--rule-dark);
  line-height: 1;
  flex-shrink: 0;
  width: 44px;
  text-align: right;
  margin-top: -4px;
}
.top5-text {}
.top5-kicker {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 10px;
  font-weight: 800;
  letter-spacing: 2px;
  text-transform: uppercase;
  color: var(--crimson);
  margin-bottom: 4px;
}
.top5-title {
  font-family: 'Playfair Display', serif;
  font-size: 16px;
  font-weight: 700;
  line-height: 1.35;
  color: var(--navy);
}
.top5-item:hover .top5-title { color: var(--crimson); }
.top5-meta {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 11px;
  font-weight: 600;
  color: var(--ink-light);
  margin-top: 4px;
}

/* ── TELUGU SECTION ── */
.telugu-section { background: var(--navy); border-radius: 4px; padding: 20px; margin-bottom: 32px; }
.telugu-section .section-head h2 { color: var(--gold); font-size: 22px; }
.telugu-section .section-head { border-bottom-color: var(--gold); }
.telugu-cards { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 14px; }
.telugu-card {
  background: rgba(255,255,255,.06);
  border: 1px solid rgba(255,255,255,.1);
  border-radius: 3px;
  padding: 14px;
  cursor: pointer;
  transition: all .2s;
}
.telugu-card:hover { background: rgba(200,16,46,.2); border-color: var(--crimson); }
.telugu-card-title {
  font-family: 'Noto Sans Telugu', sans-serif;
  font-size: 16px;
  font-weight: 700;
  color: var(--cream);
  line-height: 1.5;
  margin-bottom: 8px;
}
.telugu-card-sub {
  font-family: 'Noto Sans Telugu', sans-serif;
  font-size: 12px;
  color: rgba(255,255,255,.55);
  line-height: 1.5;
}
.telugu-card-meta {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 11px;
  font-weight: 600;
  color: var(--gold);
  margin-top: 8px;
  letter-spacing: .5px;
}

/* ── STUDENT ZONE ── */
.student-zone {
  background: linear-gradient(135deg, #0D1B2A 0%, #1A2E40 100%);
  border-radius: 4px;
  padding: 20px;
  margin-bottom: 32px;
  border: 2px solid var(--gold);
}
.student-zone .section-head h2 { color: var(--gold); }
.student-zone .section-head { border-bottom-color: var(--gold); }
.exams-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(140px, 1fr)); gap: 10px; }
.exam-card {
  background: rgba(212,175,55,.08);
  border: 1px solid rgba(212,175,55,.25);
  border-radius: 4px;
  padding: 12px;
  text-align: center;
  cursor: pointer;
  transition: all .2s;
}
.exam-card:hover { background: var(--crimson); border-color: var(--crimson); }
.exam-card .exam-icon { font-size: 28px; margin-bottom: 6px; }
.exam-card .exam-name {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 14px;
  font-weight: 800;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  color: var(--gold);
}
.exam-card .exam-date {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 11px;
  color: rgba(255,255,255,.55);
  margin-top: 3px;
}
.student-news { margin-top: 16px; display: flex; flex-direction: column; gap: 10px; }
.student-item {
  background: rgba(255,255,255,.05);
  border-left: 3px solid var(--gold);
  padding: 10px 12px;
  border-radius: 0 3px 3px 0;
  cursor: pointer;
}
.student-item:hover { background: rgba(255,255,255,.09); }
.student-item-title {
  font-family: 'Source Serif 4', serif;
  font-size: 14px;
  font-weight: 600;
  color: var(--cream);
  line-height: 1.4;
}
.student-item-meta {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 11px;
  color: var(--gold);
  margin-top: 4px;
  font-weight: 600;
  letter-spacing: .5px;
}

/* ── SIDEBAR ── */
.sidebar { display: flex; flex-direction: column; gap: 20px; }

.sidebar-widget {
  background: var(--white);
  border: 1px solid var(--rule);
  border-radius: 3px;
  overflow: hidden;
  box-shadow: var(--shadow-sm);
}
.widget-head {
  background: var(--navy);
  padding: 10px 14px;
  display: flex;
  align-items: center;
  gap: 8px;
}
.widget-head h3 {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 13px;
  font-weight: 800;
  letter-spacing: 2px;
  text-transform: uppercase;
  color: var(--gold);
  line-height: 1;
}
.widget-body { padding: 12px 14px; }

/* Markets */
.market-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 8px 0;
  border-bottom: 1px solid var(--rule);
  font-size: 13px;
}
.market-row:last-child { border-bottom: none; }
.market-name { font-family: 'Barlow Condensed', sans-serif; font-weight: 700; font-size: 13px; letter-spacing: .5px; color: var(--ink); }
.market-val { font-family: 'Barlow Condensed', sans-serif; font-size: 14px; font-weight: 700; }
.market-chg { font-family: 'Barlow Condensed', sans-serif; font-size: 12px; font-weight: 700; }
.up { color: #1A7A3C; }
.down { color: #CC2222; }

/* Trending */
.trend-item {
  display: flex;
  align-items: flex-start;
  gap: 10px;
  padding: 9px 0;
  border-bottom: 1px solid var(--rule);
  cursor: pointer;
}
.trend-item:last-child { border-bottom: none; }
.trend-num {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 20px;
  font-weight: 800;
  color: var(--rule-dark);
  flex-shrink: 0;
  width: 22px;
  line-height: 1;
}
.trend-text {
  font-family: 'Source Serif 4', serif;
  font-size: 13px;
  font-weight: 600;
  color: var(--ink);
  line-height: 1.35;
}
.trend-item:hover .trend-text { color: var(--crimson); }
.trend-count {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 11px;
  color: var(--ink-light);
  margin-top: 2px;
}

/* Weather */
.weather-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }
.weather-city {
  background: var(--cream);
  border-radius: 3px;
  padding: 8px 10px;
  text-align: center;
}
.weather-city-name {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 1px;
  text-transform: uppercase;
  color: var(--ink-light);
}
.weather-temp {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 24px;
  font-weight: 800;
  color: var(--navy);
  line-height: 1.1;
}
.weather-cond {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 11px;
  color: var(--ink-light);
}

/* Poll */
.poll-question {
  font-family: 'Source Serif 4', serif;
  font-size: 14px;
  font-weight: 600;
  color: var(--ink);
  line-height: 1.45;
  margin-bottom: 14px;
}
.poll-option {
  display: flex;
  flex-direction: column;
  gap: 3px;
  margin-bottom: 10px;
  cursor: pointer;
}
.poll-option-label {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 13px;
  font-weight: 600;
  color: var(--ink);
  display: flex;
  justify-content: space-between;
}
.poll-bar-track { height: 6px; background: var(--cream-dark); border-radius: 3px; overflow: hidden; }
.poll-bar-fill { height: 100%; background: var(--crimson); border-radius: 3px; transition: width .5s ease; }
.poll-total {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 11px;
  color: var(--ink-light);
  margin-top: 4px;
}

/* ── AI STATU
