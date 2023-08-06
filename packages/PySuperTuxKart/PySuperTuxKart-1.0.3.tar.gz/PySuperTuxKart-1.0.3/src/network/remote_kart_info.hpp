//
//  SuperTuxKart - a fun racing game with go-kart
//  Copyright (C) 2013-2015 SuperTuxKart-Team
//
//  This program is free software; you can redistribute it and/or
//  modify it under the terms of the GNU General Public License
//  as published by the Free Software Foundation; either version 3
//  of the License, or (at your option) any later version.
//
//  This program is distributed in the hope that it will be useful,
//  but WITHOUT ANY WARRANTY; without even the implied warranty of
//  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//  GNU General Public License for more details.
//
//  You should have received a copy of the GNU General Public License
//  along with this program; if not, write to the Free Software
//  Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.

/*! \file remote_kart_info.hpp
 */

#ifndef HEADER_REMOTE_KART_INFO_HPP
#define HEADER_REMOTE_KART_INFO_HPP

#include <limits>
#include <memory>
#include <string>
#include <vector>
#include <irrString.h>

enum KartTeam : int8_t
{
    KART_TEAM_NONE=-1,
    KART_TEAM_RED=0,
    KART_TEAM_BLUE=1,
};

/** Game difficulty per player. */
enum PerPlayerDifficulty : uint8_t
{
    PLAYER_DIFFICULTY_NORMAL = 0,
    PLAYER_DIFFICULTY_HANDICAP,
    PLAYER_DIFFICULTY_COUNT
};

class RemoteKartInfo
{
        std::string         m_kart_name;
        irr::core::stringw  m_user_name;
        int                 m_local_player_id;
        int                 m_global_player_id;
        uint32_t            m_host_id;
        KartTeam            m_kart_team;
        bool                m_network_player;
        PerPlayerDifficulty m_difficulty;
        float               m_default_kart_color;
        uint32_t            m_online_id;
public:
     RemoteKartInfo(int player_id, const std::string& kart_name,
                    const irr::core::stringw& user_name, uint32_t host_id,
                    bool network)
                  : m_kart_name(kart_name), m_user_name(user_name),
                    m_local_player_id(player_id), m_global_player_id(-1),
                    m_host_id(host_id), m_kart_team(KART_TEAM_NONE),
                    m_network_player(network),
                    m_difficulty(PLAYER_DIFFICULTY_NORMAL),
                    m_default_kart_color(0.0f), m_online_id(0)
     {}
     RemoteKartInfo(const std::string& kart_name) : m_kart_name(kart_name),
                    m_user_name(""), m_local_player_id(-1),
                    m_global_player_id(-1),
                    m_host_id(std::numeric_limits<uint32_t>::max()),
                    m_kart_team(KART_TEAM_NONE), m_network_player(false),
                    m_difficulty(PLAYER_DIFFICULTY_NORMAL),
                    m_default_kart_color(0.0f), m_online_id(0)
     {}
     RemoteKartInfo() : m_kart_name(""), m_user_name(""),
                    m_local_player_id(-1), m_global_player_id(-1),
                    m_host_id(std::numeric_limits<uint32_t>::max()),
                    m_kart_team(KART_TEAM_NONE), m_network_player(false),
                    m_difficulty(PLAYER_DIFFICULTY_NORMAL),
                    m_default_kart_color(0.0f), m_online_id(0)
     {}
    void setKartName(const std::string& n)   { m_kart_name = n;           }
    void setPlayerName(const irr::core::stringw& u) { m_user_name = u;    }
    void setHostId(uint32_t id)              { m_host_id = id;            }
    void setLocalPlayerId(int id)            { m_local_player_id = id;    }
    void setGlobalPlayerId(int id)           { m_global_player_id = id;   }
    void setKartTeam(KartTeam team)      { m_kart_team = team;      }
    void setNetworkPlayer(bool value)        { m_network_player = value;  }
    void setDefaultKartColor(float value) { m_default_kart_color = value; }
    void setPerPlayerDifficulty(PerPlayerDifficulty value) 
                                             { m_difficulty = value;      }
    void setOnlineId(uint32_t id)            { m_online_id = id;          }
    uint32_t getHostId() const               { return m_host_id;          }
    int  getLocalPlayerId() const            { return m_local_player_id;  }
    int  getGlobalPlayerId() const           { return m_global_player_id; }
    bool  isNetworkPlayer() const            { return m_network_player;   }
    const std::string& getKartName() const   { return m_kart_name;        }
    const irr::core::stringw& getPlayerName() const { return m_user_name; }
    KartTeam getKartTeam() const               { return m_kart_team;      }
    PerPlayerDifficulty getDifficulty() const { return m_difficulty;      }
    float getDefaultKartColor() const      { return m_default_kart_color; }
    uint32_t getOnlineId() const           { return m_online_id;          }
    bool disconnected() const               { return false; }
    bool isReserved() const
              { return m_host_id == std::numeric_limits<uint32_t>::max(); }
    void makeReserved()
    {
        m_host_id = std::numeric_limits<uint32_t>::max();
    }
    bool operator<(const RemoteKartInfo& other) const
    {
        return ((m_host_id<other.m_host_id) ||
                (m_host_id==other.m_host_id && m_local_player_id<other.m_local_player_id));
    }
};   // RemoteKartInfo

typedef std::vector<RemoteKartInfo> RemoteKartInfoList;

#endif
