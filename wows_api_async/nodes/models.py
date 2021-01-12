from pydantic import BaseModel


class Warship(BaseModel):
    tier: int
    type: str
    name: str
    ship_id: int
    nation: str


class ClanInfo(BaseModel):
    members_count: int
    created_at: int
    clan_id: int
    tag: str
    name: str


class ClanDetails(BaseModel):
    members_ids: list[int]


class PlayerBattleStatistics(BaseModel):
    battles: int
    capture_points: int
    dropped_capture_points: int
    frags: int
    losses: int
    survived_battles: int
    survived_wins: int
    team_capture_points: int
    team_dropped_capture_points: int
    damage_scouting: int
    max_damage_scouting: int
    control_captured_points: int = None
    control_dropped_points: int = None


class PlayerStatistics(BaseModel):
    pvp: PlayerBattleStatistics
    last_battle_time: int
    ship_id: int


class AccountInfo(BaseModel):
    account_id: int
    nickname: str
    statistics: PlayerStatistics = None


class Ship(BaseModel):
    name: str
    ship_id: int
    tier: int
    type: str


class Achievements(BaseModel):
    airdefenseexpert: int = 0
    all_three_halloween_complete: int = 0
    amauteur: int = 0
    arsonist: int = 0
    atb_winner: int = 0
    atba_caliber: int = 0
    avacommon: int = 0
    avasharks: int = 0
    battle_hero: int = 0
    bd2016_festiv_soup: int = 0
    bd2016_fireshow: int = 0
    bd2016_king_of_party: int = 0
    bd2016_manners: int = 0
    bd2016_party_animal: int = 0
    bd2016_party_check_in: int = 0
    bd2016_rise_of_the_machines: int = 0
    bd2016_run_forest: int = 0
    bd2016_snatch: int = 0
    bd2016_wrong_sow: int = 0
    bd2_arp: int = 0
    bd2_bismarck: int = 0
    bd2_campaigns: int = 0
    bd2_containers: int = 0
    bd2_credits: int = 0
    bd2_crew: int = 0
    bd2_gb: int = 0
    bd2_ny2016: int = 0
    bd2_ranks: int = 0
    campaign1_completed: int = 0
    campaign1_completed_excellent: int = 0
    campaign_bismarck_completed: int = 0
    campaign_halsey_completed: int = 0
    campaign_jerzy_swirski_completed: int = 0
    campaign_newyear2018basic_completed: int = 0
    campaign_newyear2019pef_completed: int = 0
    campaign_ny17b_completed: int = 0
    campaign_ny17b_completed_excellent: int = 0
    campaign_sb_completed: int = 0
    campaign_vivelafrance_completed: int = 0
    campaign_yamamoto_completed: int = 0
    capital: int = 0
    chief_engineer: int = 0
    clan_season_1_league_1: int = 0
    clan_season_1_league_2: int = 0
    clan_season_1_league_3: int = 0
    clan_season_1_league_4: int = 0
    clear_sky: int = 0
    collection_americanarc_completed: int = 0
    collection_bismarck_completed: int = 0
    collection_britisharc_completed: int = 0
    collection_dunkirk_completed: int = 0
    collection_happy_birthday2018_completed: int = 0
    collection_happynewyear2018_completed: int = 0
    collection_happynewyear2019_completed: int = 0
    collection_hsf2018_completed: int = 0
    collection_ovechkin_completed: int = 0
    collection_vivelafrance_completed: int = 0
    collection_wowsbirthday_completed: int = 0
    collection_yamamoto_completed: int = 0
    cvc_brawl_top100: int = 0
    detonated: int = 0
    double_kill: int = 0
    dreadnought: int = 0
    engineer: int = 0
    ev_post_apocalypse2019_winner: int = 0
    fighter: int = 0
    fillalbum_azurlane_completed: int = 0
    fillalbum_brit_cvarc_completed: int = 0
    fillalbum_capt_completed: int = 0
    fillalbum_frenchdd_completed: int = 0
    fillalbum_gf097_completed: int = 0
    fillalbum_itca_completed: int = 0
    fillalbum_ny20_completed: int = 0
    fillalbum_sovietbb_completed: int = 0
    fireproof: int = 0
    first_blood: int = 0
    foolsday_poekhali: int = 0
    foolsday_trooper: int = 0
    glory: int = 0
    greateeight: int = 0
    halloween_2016: int = 0
    halloween_2017: int = 0
    halloween_2018: int = 0
    headbutt: int = 0
    honor: int = 0
    instant_kill: int = 0
    jollyroger: int = 0
    junior_planner: int = 0
    liquidator: int = 0
    main_caliber: int = 0
    mercenary: int = 0
    mercenary_l: int = 0
    messenger: int = 0
    messenger_l: int = 0
    millionair: int = 0
    never_enough_money: int = 0
    no_day_without_adventure: int = 0
    no_day_without_adventure_l: int = 0
    no_price_for_heroism: int = 0
    ny17_500_leagues: int = 0
    ny17_aiming: int = 0
    ny17_break_the_bank: int = 0
    ny17_dress_the_tree: int = 0
    ny17_safecracker: int = 0
    ny17_to_the_bottom: int = 0
    ny17_win_all: int = 0
    ny17_win_at_least_one: int = 0
    one_soldier_in_the_field: int = 0
    pve_dunkerque_operation_dynamo: int = 0
    pve_hero_dam_enem: int = 0
    pve_hero_win_one: int = 0
    pve_hon_done_class: int = 0
    pve_hon_frag_class: int = 0
    pve_hon_pr_save_1: int = 0
    pve_hon_pr_save_2: int = 0
    pve_hon_win_all_done: int = 0
    retribution: int = 0
    science_of_winning_arsonist: int = 0
    science_of_winning_bombardier: int = 0
    science_of_winning_hard_edged: int = 0
    science_of_winning_lucky: int = 0
    science_of_winning_tactician: int = 0
    science_of_winning_to_the_bottom: int = 0
    sea_legend: int = 0
    stream: int = 0
    support: int = 0
    top_league_clan_season_10: int = 0
    top_league_clan_season_2: int = 0
    twitch_wg: int = 0
    unsinkable: int = 0
    veteran: int = 0
    victory: int = 0
    warrior: int = 0
    withering: int = 0
    workaholic: int = 0
    workaholic_l: int = 0
